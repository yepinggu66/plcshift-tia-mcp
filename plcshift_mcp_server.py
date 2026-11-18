#!/usr/bin/env python3
"""
PLCShift Global — MCP Server for Cross-Brand PLC I/O Tag Remapping & S7-1500 SCL Migration
Connects Claude Desktop / Cursor to the PLCShift deterministic TIA Portal V19 compiler API.
"""
import sys
import json
import urllib.request

API_URL = "https://pingguye.cn/stackverdict/api/plcshift/analyze"

def call_plcshift_api(vendor_id: str, custom_tags_csv: str = "", custom_legacy_code: str = ""):
    payload = {
        "vendorId": vendor_id,
        "customTagsCsv": custom_tags_csv or None,
        "customLegacyCode": custom_legacy_code or None,
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode("utf-8"))

def handle_jsonrpc(req):
    method = req.get("method", "")
    req_id = req.get("id")
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "plcshift-tia-copilot", "version": "1.0.0"},
            },
        }
    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "migrate_plc_tags_and_code",
                        "description": "Converts Rockwell Studio 5000 CSV, Mitsubishi Hex X/Y/D, or Legacy S7-300 AWL/STL into even-byte aligned Siemens TIA Portal V19 XML Tag Tables and IEC 61131-3 S7-1500 SCL code.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "vendor_id": {
                                    "type": "string",
                                    "enum": ["rockwell-studio5000", "mitsubishi-gx", "siemens-s7-300"],
                                    "default": "rockwell-studio5000",
                                },
                                "custom_tags_csv": {"type": "string"},
                                "custom_legacy_code": {"type": "string"},
                            },
                        },
                    }
                ]
            },
        }
    if method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        res = call_plcshift_api(
            args.get("vendor_id", "rockwell-studio5000"),
            args.get("custom_tags_csv", ""),
            args.get("custom_legacy_code", ""),
        )
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2, ensure_ascii=False)}]},
        }
    return {"jsonrpc": "2.0", "id": req_id, "result": {}}

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            q = json.loads(line)
            if "id" in q:
                sys.stdout.write(json.dumps(handle_jsonrpc(q)) + "\n")
                sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")
