# 🏭 PLCShift Global — Cross-Brand PLC Migration & Siemens TIA Portal V19 XML / SCL AI Copilot (MCP Server)

[![Live Workbench](https://img.shields.io/badge/Live_Workbench-PLCShift_Global-f59e0b?style=for-the-badge)](https://pingguye.cn/stackverdict/plcshift)
[![TIA Portal](https://img.shields.io/badge/Siemens_TIA_Portal-V18_%2F_V19_Openness_XML-009999?style=for-the-badge)](https://pingguye.cn/stackverdict/plcshift)
[![IEC 61131-3](https://img.shields.io/badge/IEC_61131--3-S7--1500_SCL-blue?style=for-the-badge)](https://pingguye.cn/stackverdict/plcshift)

**PLCShift Global** is a deterministic cross-brand PLC I/O tag compiler, non-overlapping byte-alignment engine, and legacy `AWL/STL/L5X` to **Siemens SIMATIC S7-1500 / S7-1200 (TIA Portal V18/V19)** migration copilot.

👉 **Try the Live Browser Workbench (Zero Login Required):** **[https://pingguye.cn/stackverdict/plcshift](https://pingguye.cn/stackverdict/plcshift)**

---

## ⚡ Core Industrial Capabilities

1. **Rockwell Allen-Bradley (Studio 5000 CSV / L5X) ➔ Siemens TIA Portal V19**
   - Automatically maps flat ControlLogix / CompactLogix slot tags (`Local:1:I.Data.0`, `Local:3:O.Ch0Data`, `DINT`, `REAL`) into even-byte aligned Siemens `%I`, `%Q`, `%IW`, `%QW`, `%MW`, and `%MD` addresses without memory boundary overlaps.
2. **Mitsubishi MELSEC FX / Q (Base-16 Hex & Base-8 Octal) ➔ Siemens S7-1200/1500**
   - Translates hexadecimal `X00–X1F` / `Y00–Y1F` and `D/M` registers into strict IEC 61131-3 byte.bit (`%I0.0`, `%Q1.0`) addressing.
3. **Legacy Siemens S7-300/400 (STEP 7 AWL/STL) ➔ S7-1500 Symbolic SCL**
   - Detects non-migratable `LAR1 / P#DBX` indirect pointer arithmetic, `S5TIME` BCD timers, `PIW/PQW` peripheral words, and `FB41 CONT_C` PID loops, refactoring them into modern `S7_Optimized_Access` `FUNCTION_BLOCK` SCL code and `PID_Compact` technology objects.
4. **1-Click TIA Portal Openness V19 `<SW.Tags.PlcTagTable>` XML Export**
   - Generates schema-validated XML tag tables ready for direct import into Siemens TIA Portal V18/V19.

---

## 🔌 Use as an MCP Server in Claude Desktop / Cursor

Add the following to your `.cursor/mcp.json` or `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "plcshift-tia-copilot": {
      "command": "python",
      "args": ["plcshift_mcp_server.py"],
      "env": {
        "PLCSHIFT_API_ENDPOINT": "https://pingguye.cn/stackverdict/api/plcshift/analyze"
      }
    }
  }
}
```

## 🛠️ Need Full-Project Turnkey PLC Migration?
For System Integrators (SIs) and manufacturing plants migrating full `.L5X`, `.AWL`, `.MWP`, or `.ZAP19` archives, request a turnkey engineering quote or SI Team License at **[https://pingguye.cn/stackverdict/plcshift](https://pingguye.cn/stackverdict/plcshift)**.
