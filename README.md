# 🏭 PLCShift Global & WeFish EquipAI — Industrial PLC Migration & Plant Equipment Crisis Pre-Simulation OS

[![Live Workbench](https://img.shields.io/badge/Live_Workbench-PLCShift_Global-f59e0b?style=for-the-badge)](https://pingguye.cn/stackverdict/plcshift)
[![WeFish EquipAI](https://img.shields.io/badge/Plant_OS-WeFish_EquipAI-10b981?style=for-the-badge)](https://pingguye.cn/stackverdict/magfactory)
[![TIA Portal](https://img.shields.io/badge/Siemens_TIA_Portal-V18_%2F_V19_Openness_XML-009999?style=for-the-badge)](https://pingguye.cn/stackverdict/plcshift)
[![IEC 61131-3](https://img.shields.io/badge/IEC_61131--3-S7--1500_SCL-blue?style=for-the-badge)](https://pingguye.cn/stackverdict/plcshift)

**PLCShift Global & WeFish EquipAI** is a deterministic industrial intelligence platform built on 20+ years of plant equipment director experience (managing 115+ heavy industrial units, NdFeB vacuum sintering furnaces, strip casting, and jet mills).

It provides:
1. **Cross-Brand PLC Tag & Logic Refactoring** (Rockwell Allen-Bradley / Mitsubishi ➔ Siemens SIMATIC S7-1500 / TIA Portal V19 SCL & Openness XML).
2. **WeFish EquipAI Plant Operating System** (Air-gapped M1–M10 Equipment TPM, micro-vacuum leak rate early-warning, and automated 8D root-cause quality traceability).

---

## ⚡ Live Interactive Workbenches (Zero Login Required)

- 👉 **PLC Migration & SCL Engine:** **[https://pingguye.cn/stackverdict/plcshift](https://pingguye.cn/stackverdict/plcshift)**
- 👉 **WeFish EquipAI Crisis Pre-Simulation Sandbox:** **[https://pingguye.cn/stackverdict/magfactory](https://pingguye.cn/stackverdict/magfactory)**

---

## 🛠️ Core Capabilities

### 1. Rockwell Allen-Bradley (Studio 5000 CSV / L5X) ➔ Siemens TIA Portal V19
- Automatically maps flat ControlLogix / CompactLogix slot tags (`Local:1:I.Data.0`, `Local:3:O.Ch0Data`, `DINT`, `REAL`) into even-byte aligned Siemens `%I`, `%Q`, `%IW`, `%QW`, `%MW`, and `%MD` addresses without memory boundary overlaps.

### 2. Mitsubishi MELSEC FX / Q (Base-16 Hex & Base-8 Octal) ➔ Siemens S7-1200/1500
- Translates hexadecimal `X00–X1F` / `Y00–Y1F` and `D/M` registers into strict IEC 61131-3 byte.bit (`%I0.0`, `%Q1.0`) addressing.

### 3. Legacy Siemens S7-300/400 (STEP 7 AWL/STL) ➔ S7-1500 Symbolic SCL
- Detects non-migratable `LAR1 / P#DBX` indirect pointer arithmetic, `S5TIME` BCD timers, `PIW/PQW` peripheral words, and `FB41 CONT_C` PID loops, refactoring them into modern `S7_Optimized_Access` `FUNCTION_BLOCK` SCL code and `PID_Compact` technology objects.

### 4. 1-Click TIA Portal Openness V19 `<SW.Tags.PlcTagTable>` XML Export
- Generates schema-validated XML tag tables ready for direct import into Siemens TIA Portal V18/V19.

### 5. WeFish EquipAI: Sintering Micro-Vacuum Leak Early Warning ($10^{-3} \to 10^{-1}$ Pa)
- Real-time early warning algorithms for vacuum leakage rates and thermal gradient anomalies in sintering furnaces, preventing multi-ton rare-earth magnet oxidation and $25k–$50k batch scrap losses.

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

---

## 💼 Commercial Licensing & Turnkey Engineering Buyout

We operate strictly under an **"Evaluate on Cloud Sandbox · Full Source Code Wire Buyout · Zero Trial Ware"** policy.

| Tier | Commercial Package | Pricing (USD / RMB) | Deliverables & Value |
| :--- | :--- | :--- | :--- |
| **Tier 2** | **4-in-1 Air-Gapped Single-Plant Buyout** | **$18,800 USD<br>(¥135,000 RMB)** | • Complete system source code (Python, Next.js, SQLite/PostgreSQL)<br>• Micro-vacuum leak detection algorithm library<br>• 20-Year Plant Director 31-SOP & Checkpoint system (Word/Excel commercial rights)<br>• 100% on-premise air-gapped deployment (zero cloud dependencies)<br>• 1-Year remote principal architect technical handover |
| **Tier 3** | **Enterprise Multi-Plant + 20-Yr Advisory Turnkey** | **$58,000+ USD<br>(¥418,000+ RMB)** | • Multi-plant cluster deployment (up to 300 users)<br>• Custom proprietary furnace/press PLC protocol integration<br>• On-site equipment department overhaul & anti-fraud inspection setup<br>• Automotive OEM Tier-1 audit preparation & 8D CAPA coaching<br>• Dedicated 24/7 technical escalation & lifetime upgrade roadmapping |

Direct Inquiry & Turnkey Contract:
- Live Interactive Sandbox: [https://pingguye.cn/stackverdict/magfactory](https://pingguye.cn/stackverdict/magfactory)
- Official Technical Email: **`yepinggu66@gmail.com`**
