# ECA1011 — Microprocessors and Microcontrollers

**Student Name:** Naga Jaswanth B  
**Register Number:** 192424300  
**Experiment:** 1 — 8-Bit and 16-Bit Arithmetic Operations Using the Intel 8085 Microprocessor

---


## 1. Overview & Objective

This directory contains the source code, execution evidence, and final submission report for **Experiment 1: Analysis, Development, and Verification of 8-Bit and 16-Bit Arithmetic Operations Using Assembly Language Programming** on the **Intel 8085 Microprocessor**.

The objective of this laboratory experiment is to design, assemble, execute, and verify eight fundamental arithmetic routines covering addition, subtraction, multiplication, and division for both 8-bit and 16-bit unsigned operands, including proper handling of status flags (Carry, Auxiliary Carry, Parity, Sign, Zero), multi-byte carry propagation, and quotient/remainder calculations.

---

## 2. Simulation Environment

All programs were developed, assembled, and executed using the **Microprocessor 8085 Simulator Software Kit 1.0**.

* **Microprocessor**: Intel 8085 (8-bit architecture, 16-bit memory addressing).
* **Execution & Evidence**: Each program was assembled to its designated memory address, loaded with test vectors in User Data RAM (`4500H–453FH`), executed to completion (`HLT`), and verified through genuine full-window simulator screen captures.

---

## 3. Project Structure

```text
Experiment_1/
├── Programs/                                 # Intel 8085 assembly source programs (.mpc)
│   ├── A(1) — 8-bit Addition.mpc
│   ├── A(2) — 8-bit Subtraction.mpc
│   ├── B(1) — 16-bit Addition.mpc
│   ├── B(2) — 16-bit Subtraction.mpc
│   ├── C(1) — 8-bit Multiplication.mpc
│   ├── C(2) — 8-bit Division.mpc
│   ├── D(1) — 16-bit Multiplication.mpc
│   └── D(2) — 16-bit Division.mpc
├── Evidence/                                 # Genuine simulator execution screenshots
│   ├── A(1) — 8-bit Addition.png
│   ├── A(2) — 8-bit Subtraction.png
│   ├── B(1) — 16-bit Addition.png
│   ├── B(2) — 16-bit Subtraction.png
│   ├── C(1) — 8-bit Multiplication.png
│   ├── C(2) — 8-bit Division.png
│   ├── D(1) — 16-bit Multiplication.png
│   └── D(2) — 16-bit Division.png
├── Experiment_1_8085_Arithmetic_Operations_Final.docx  # Authoritative final laboratory report
└── README.md                                 # Experiment documentation
```

*(Note: Local development scripts, validation utilities, and intermediate logs are maintained locally for workflow verification and reproducibility).*

---

## 4. Program Inventory & Verification Matrix

All eight programs strictly comply with the authoritative laboratory specification and have been confirmed against genuine execution results:

| ID | Section | Module Name | Start Addr | Input Addresses & Values | Expected & Observed Outputs | Output Status | Evidence Screenshot |
| :---: | :---: | :--- | :---: | :--- | :--- | :---: | :---: |
| **A1** | A(1) | 8-bit Addition | `4100H` | `4500H = 9CH`, `4501H = 7AH` | `4502H = 16H`, `4503H = 01H`, `4504H = 11H` | **PASS** | `Evidence/A(1) — 8-bit Addition.png` (Fig A-1) |
| **A2** | A(2) | 8-bit Subtraction | `4100H` | `4500H = 9CH`, `4501H = 7AH` | `4505H = 22H`, `4506H = 00H`, `4507H = 14H` | **PASS** | `Evidence/A(2) — 8-bit Subtraction.png` (Fig A-2) |
| **B1** | B(1) | 16-bit Addition | `4200H` | `4510H..4513H = 34H, 12H, 78H, 56H` | `4514H = ACH`, `4515H = 68H`, `4516H = 00H` | **PASS** | `Evidence/B(1) — 16-bit Addition.png` (Fig B-1) |
| **B2** | B(2) | 16-bit Subtraction | `4200H` | `4510H..4513H = 34H, 12H, 78H, 56H` | `4518H = BCH`, `4519H = BBH`, `451AH = 01H` | **PASS** | `Evidence/B(2) — 16-bit Subtraction.png` (Fig B-2) |
| **C1** | C(1) | 8-bit Multiplication | `4300H` | `4520H = 12H`, `4521H = 05H` | `4522H = 5AH`, `4523H = 00H` | **PASS** | `Evidence/C(1) — 8-bit Multiplication.png` (Fig C-1) |
| **C2** | C(2) | 8-bit Division | `4300H` | `4524H = 64H`, `4525H = 05H` | `4526H = 14H`, `4527H = 00H` | **PASS** | `Evidence/C(2) — 8-bit Division.png` (Fig C-2) |
| **D1** | D(1) | 16-bit Multiplication | `4400H` | `4530H..4533H = 34H, 12H, 78H, 56H` | `4534H..4537H = 60H, 00H, 26H, 06H` | **PASS** | `Evidence/D(1) — 16-bit Multiplication.png` (Fig D-1) |
| **D2** | D(2) | 16-bit Division | `442DH` *(Base 4400H)* | `4538H..453BH = 78H, 56H, 34H, 12H` | `453CH..453FH = 04H, 00H, A8H, 0DH` | **PASS** | `Evidence/D(2) — 16-bit Division.png` (Fig D-2) |

---

## 5. Technical Specifications by Section

### Section A — 8-Bit Arithmetic (`4100H`)
* **A(1) 8-Bit Addition**: Operands `9CH` (156) and `7AH` (122) yield sum `116H` (278 decimal). The Accumulator receives `16H`, Carry flag `CY = 1`, Auxiliary Carry `AC = 1`, Parity `P = 0`, producing a Processor Status Word (PSW) flag byte of `11H` saved at `4504H`.
* **A(2) 8-Bit Subtraction**: Minuend `9CH` and Subtrahend `7AH` yield difference `22H` (34 decimal). No borrow is generated (`CY = 0`), Auxiliary Borrow `AC = 1`, Parity `P = 1`, producing a PSW flag byte of `14H` saved at `4507H`.

### Section B — 16-Bit Arithmetic (`4200H`)
* **B(1) 16-Bit Addition**: Operands $X = 1234\text{H}$ and $Y = 5678\text{H}$ are added using register pair addition (`DAD B`). Sum is $68\text{ACH}$ with carry $00\text{H}$. Stored as `4514H = ACH`, `4515H = 68H`, `4516H = 00H`.
* **B(2) 16-Bit Subtraction**: Operand $Y = 5678\text{H}$ is subtracted from $X = 1234\text{H}$. The operation yields $1234\text{H} - 5678\text{H} = \text{BBBCH}$ using 16-bit unsigned wraparound, generating a borrow of $01\text{H}$. Low byte subtraction ($34\text{H} - 78\text{H} = \text{BCH}$) sets borrow; high byte subtraction with borrow ($12\text{H} - 56\text{H} - 1 = \text{BBH}$) sets the final borrow flag $01\text{H}$ at `451AH`.

### Section C — 8-Bit Multiplication & Division (`4300H`)
* **C(1) 8-Bit Multiplication**: Multiplicand $12\text{H}$ (18) is multiplied by multiplier $05\text{H}$ (5) using repeated addition. The 16-bit product $005\text{AH}$ (90 decimal) is stored at `4522H = 5AH` and `4523H = 00H`.
* **C(2) 8-Bit Division**: Dividend $64\text{H}$ (100) is divided by divisor $05\text{H}$ (5) via repeated subtraction. The resulting Quotient $14\text{H}$ (20 decimal) is stored at `4526H` and Remainder $00\text{H}$ is stored at `4527H`.

### Section D — 16-Bit Multiplication & Division (`4400H`)
* **D(1) 16-Bit Multiplication**: Multiplies $1234\text{H}$ by $5678\text{H}$ using 32-bit multi-byte repeated addition with four accumulator bytes. Produces full 32-bit product $06260060\text{H}$ across `4534H = 60H`, `4535H = 00H`, `4536H = 26H`, `4537H = 06H`.
* **D(2) 16-Bit Division**: Divides 16-bit dividend $5678\text{H}$ by 16-bit divisor $1234\text{H}$ via repeated 16-bit subtraction. Assembled at routine entry `442DH` within the Section D block (`4400H`). Yields Quotient $= 0004\text{H}$ (`453CH = 04H`, `453DH = 00H`) and Remainder $= 0\text{DA}8\text{H}$ (`453EH = A8H`, `453FH = 0DH`).

---

## 6. Final Submission Report

The authoritative final laboratory document is:
* **[`Experiment_1_8085_Arithmetic_Operations_Final.docx`](Experiment_1_8085_Arithmetic_Operations_Final.docx)**

This document conforms strictly to college laboratory formatting standards, containing complete assembly source code listings, algorithmic descriptions, memory mapping tables, theoretical calculations, and embedded genuine simulator execution evidence for all eight modules.
