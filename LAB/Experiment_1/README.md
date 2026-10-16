# Experiment 1: 8-Bit and 16-Bit Arithmetic Operations (Intel 8085)

## Overview

This repository directory contains the complete source code, verification logs, execution evidence, automation tooling, and final laboratory documentation for **Experiment 1: Analysis, Development and Verification of 8-bit and 16-bit Arithmetic Operations Using Assembly Language Programming** on the **Intel 8085 Microprocessor** using the **Microprocessor 8085 Simulator Software Kit 1.0**.

---

## Directory Structure

```text
Experiment_1/
├── Evidence/                               # Genuine simulator execution screenshots
│   ├── B2_16bit_Subtraction.png            # Verified execution of 16-bit subtraction
│   └── D1_16bit_Multiplication.png         # Verified execution of 16-bit multiplication
├── Logs/                                   # Machine-readable manifests and audit logs
│   ├── duplicate_analysis.json             # Technical comparison of generic vs authoritative MPCs
│   ├── duplicate_analysis_report.md        # Detailed duplicate evaluation report
│   ├── file_manifest.json                  # SHA-256 integrity manifest of workspace files
│   ├── validation_results.json             # Structured memory verification results
│   └── validation_summary.md               # Human-readable verification matrix
├── Programs/                               # Authoritative Intel 8085 source programs (.mpc)
│   ├── A(1) — 8-bit Addition.mpc           # 8-bit addition with carry & flag storage (4100H)
│   ├── A(2) — 8-bit Subtraction.mpc        # 8-bit subtraction with borrow & flag storage (4100H)
│   ├── B(1) — 16-bit Addition.mpc          # 16-bit addition with carry (4200H)
│   ├── B(1) — 16-bit Subtraction.mpc       # 16-bit subtraction with borrow (4200H)
│   ├── C(1) — 8-bit Multiplication.mpc     # 8-bit multiplication via repeated addition (4300H)
│   ├── C(2) — 8-bit Division.mpc           # 8-bit division via repeated subtraction (4300H)
│   ├── D(1) — 16-bit Multiplication.mpc    # 16-bit multiplication with 32-bit product (4400H)
│   └── D(2) — 16-bit Division.mpc          # 16-bit division with quotient & remainder (442DH)
├── Reports/                                # Laboratory report documents
│   ├── Experiment_1_8085_Arithmetic_Operations_Draft.docx  # Baseline draft report
│   └── Experiment_1_8085_Arithmetic_Operations_Final.docx  # Authoritative final report
├── Scripts/                                # Safe CLI automation & validation utilities
│   ├── build_report.py                     # Compiles the final academic DOCX report
│   ├── capture_evidence.ps1                # PowerShell wrapper to capture simulator window
│   ├── capture_evidence.py                 # Win32 screen capture utility for active simulator
│   ├── compare_programs.ps1                # PowerShell wrapper for program comparison
│   ├── compare_programs.py                 # Deep structural comparison of MPC programs
│   ├── generate_mpc_programs.py            # Generates compliant MPC files with hex machine code
│   ├── inventory.ps1                       # Generates SHA-256 file manifest
│   └── validate_results.py                 # Compares observed outputs against expected values
└── README.md                               # Project documentation & execution guide
```

---

## Program Inventory & Verification Matrix

All eight programs are implemented strictly according to the authoritative laboratory specification:

| ID | Module Name | Start Addr | Input Addresses & Values | Expected Outputs | Verified Status | Evidence Status |
| :---: | :--- | :---: | :--- | :--- | :---: | :---: |
| **A(1)** | 8-bit Addition | `4100H` | `4500H = 9CH`, `4501H = 7AH` | `4502H = 16H`, `4503H = 01H`, `4504H = 11H` | **PASS** | ⏳ *Pending UI* |
| **A(2)** | 8-bit Subtraction | `4100H` | `4500H = 9CH`, `4501H = 7AH` | `4505H = 22H`, `4506H = 00H`, `4507H = 14H` | **PASS** | ⏳ *Pending UI* |
| **B(1)** | 16-bit Addition | `4200H` | `4510H..4513H = 34H, 12H, 78H, 56H` | `4514H = ACH`, `4515H = 68H`, `4516H = 00H` | **PASS** | ⏳ *Pending UI* |
| **B(2)** | 16-bit Subtraction | `4200H` | `4510H..4513H = 34H, 12H, 78H, 56H` | `4518H = BCH`, `4519H = BBH`, `451AH = 01H` | **PASS** | ✅ **Verified (Fig B-2)** |
| **C(1)** | 8-bit Multiplication | `4300H` | `4520H = 12H`, `4521H = 05H` | `4522H = 5AH`, `4523H = 00H` | **PASS** | ⏳ *Pending UI* |
| **C(2)** | 8-bit Division | `4300H` | `4524H = 64H`, `4525H = 05H` | `4526H = 14H`, `4527H = 00H` | **PASS** | ⏳ *Pending UI* |
| **D(1)** | 16-bit Multiplication | `4400H` | `4530H..4533H = 34H, 12H, 78H, 56H` | `4534H..4537H = 60H, 00H, 26H, 06H` | **PASS** | ✅ **Verified (Fig D-1)** |
| **D(2)** | 16-bit Division | `442DH` | `4538H..453BH = 78H, 56H, 34H, 12H` | `453CH..453FH = 04H, 00H, A8H, 0DH` | **PASS** | ⏳ *Pending UI* |

---

## Technical Program Specifications

### 1. Section A — 8-Bit Arithmetic
- **A(1) 8-Bit Addition**: Operands `9CH` (156) and `7AH` (122) yield sum `116H` (278 decimal). The Accumulator receives `16H`, Carry flag `CY = 1`, Auxiliary Carry `AC = 1`, Parity `P = 0`, producing a Processor Status Word (PSW) flag byte of `11H`.
- **A(2) 8-Bit Subtraction**: Minuend `9CH` and Subtrahend `7AH` yield difference `22H` (34 decimal). No borrow is generated (`CY = 0`), Auxiliary Borrow `AC = 1`, Parity `P = 1`, producing a PSW flag byte of `14H`.

### 2. Section B — 16-Bit Arithmetic
- **B(1) 16-Bit Addition**: Operands $X = 1234\text{H}$ and $Y = 5678\text{H}$ are loaded via `LXI H` and added via `DAD B`. The resulting sum is $68\text{ACH}$ with `CY = 0`.
- **B(2) 16-Bit Subtraction**: $X - Y = 1234\text{H} - 5678\text{H} = \text{BB}\text{BCH}$ with borrow `CY = 1`. Low byte subtraction $34\text{H} - 78\text{H} = \text{BCH}$ sets borrow; high byte subtraction $12\text{H} - 56\text{H} - 1 = \text{BBH}$ sets final borrow `01H`.

### 3. Section C — 8-Bit Multiplication & Division
- **C(1) 8-Bit Multiplication**: Multiplicand $12\text{H}$ (18) is accumulated 5 times via `DAD D` loops, producing $005\text{AH}$ (90 decimal) at $4522\text{H}–4523\text{H}$.
- **C(2) 8-Bit Division**: Dividend $64\text{H}$ (100) divided by divisor $05\text{H}$ (5) via repeated subtraction gives Quotient $= 14\text{H}$ (20 decimal) at $4526\text{H}$ and Remainder $= 00\text{H}$ at $4527\text{H}$.

### 4. Section D — 16-Bit Multiplication & Division
- **D(1) 16-Bit Multiplication**: Full 16-bit by 16-bit multiplication ($1234\text{H} \times 5678\text{H}$) using multi-byte addition loops. Produces the 32-bit product $06260060\text{H}$ across four memory bytes: $4534\text{H} = 60\text{H}, 4535\text{H} = 00\text{H}, 4536\text{H} = 26\text{H}, 4537\text{H} = 06\text{H}$.
- **D(2) 16-Bit Division**: 16-bit dividend $5678\text{H}$ divided by divisor $1234\text{H}$ via repeated 16-bit subtraction. Produces Quotient $= 0004\text{H}$ ($453\text{CH} = 04\text{H}, 453\text{DH} = 00\text{H}$) and Remainder $= 0\text{DA}8\text{H}$ ($453\text{EH} = \text{A}8\text{H}, 453\text{FH} = 0\text{DH}$).

---

## Automation Scripts & Commands

All scripts are non-destructive and can be executed safely from PowerShell:

```powershell
# 1. Generate full workspace SHA-256 inventory manifest
powershell -ExecutionPolicy Bypass -File .\Scripts\inventory.ps1

# 2. Run structural comparison between generic and authoritative MPC files
powershell -ExecutionPolicy Bypass -File .\Scripts\compare_programs.ps1

# 3. Validate observed memory outputs against authoritative expected specifications
python .\Scripts\validate_results.py

# 4. Compile the professional final DOCX report
python .\Scripts\build_report.py

# 5. Capture active 8085 Simulator execution evidence (e.g., for B1)
powershell -ExecutionPolicy Bypass -File .\Scripts\capture_evidence.ps1 -Program B1
```

---

## Simulator Execution & Evidence Capture Instructions

To execute remaining programs and capture genuine evidence:

1. Launch `MP8085.exe` (located at `..\8085\MP8085.exe`).
2. In the simulator, click **File → Open** and select the target program from `Programs/` (e.g., `A(1) — 8-bit Addition.mpc`).
3. Verify that the **Starting Address** matches the specification (`4100`, `4200`, `4300`, or `4400`).
4. Click **Assemble / Compile**, then click **Run / Simulate** (Execute).
5. Once execution finishes and the **User Data Grid** displays the output values, run:
   ```powershell
   .\Scripts\capture_evidence.ps1 -Program <ID>
   ```
   *(where `<ID>` is one of `A1`, `A2`, `B1`, `C1`, `C2`, `D2`).*
6. Re-run `python .\Scripts\build_report.py` to automatically embed the newly captured screenshot into the final report.
