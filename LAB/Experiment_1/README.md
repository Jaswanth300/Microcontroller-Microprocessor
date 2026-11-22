# Experiment 1: Analysis, development & verification of 8 bit, 16 bit operations using assembly language.

**Student Name:** Naga Jaswanth  
**Register Number:** 192424300  
**Course Code:** ECA1011 — Microprocessors and Microcontrollers  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences  
**Lab Date:** 15/11/26  
**Status:** `Completed & Verified ✅`

---

## 📌 Experiment Overview
This laboratory module covers fundamental arithmetic operations using the **Intel 8085 Microprocessor** instruction set. The objective is to analyze, implement, and verify low-level assembly language routines for 8-bit and 16-bit addition, subtraction, multiplication, and division, paying close attention to carry/borrow propagation, register pairs (`BC`, `DE`, `HL`), and status flags.

---

## 📂 Directory Contents

| Folder | Description | Key Files |
|:---|:---|:---|
| **`Programs/`** | Assembly source programs (`.mpc` format) | `A1_8bit_Addition.mpc`, `A2_8bit_Subtraction.mpc`, `B1_16bit_Addition.mpc`, `B2_16bit_Subtraction.mpc`, `C1_8bit_Multiplication.mpc`, `C2_8bit_Division.mpc`, `D1_16bit_Multiplication.mpc`, `D2_16bit_Division.mpc` |
| **`Evidence/`** | 8085 Simulator Software Kit 1.0 captures | `A(1) — 8-bit Addition.png`, `A(2) — 8-bit Subtraction.png`, `B(1) — 16-bit Addition.png`, `B(2) — 16-bit Subtraction.png`, `C(1) — 8-bit Multiplication.png`, `C(2) — 8-bit Division.png`, `D(1) — 16-bit Multiplication.png`, `D(2) — 16-bit Division.png` |
| **`Reports/`** | Formatted submission lab report | `Experiment_1_Analysis,_development_&_verifi.docx` |

---

## 🔬 Program Index & Memory Map

| Program | Operation | Input Address(es) | Sample Data | Output Address(es) | Result Verified | Flags Evaluated |
|:---|:---|:---|:---|:---|:---|:---|
| **A(1)** | 8-bit Addition | `4150H`, `4151H` | `12H`, `24H` | `4152H` (Sum), `4153H` (Carry) | `Sum = 36H, CY = 00H` | `CY`, `Z`, `S`, `P` |
| **A(2)** | 8-bit Subtraction | `4150H`, `4151H` | `36H`, `12H` | `4152H` (Diff), `4153H` (Borrow) | `Diff = 24H, Borrow = 00H` | `CY`, `Z`, `S`, `P` |
| **B(1)** | 16-bit Addition | `4150H-4153H` | `1234H`, `2345H` | `4154H-4155H` | `Sum = 3579H, CY = 00H` | `CY` |
| **B(2)** | 16-bit Subtraction | `4150H-4153H` | `3579H`, `1234H` | `4154H-4155H` | `Diff = 2345H, Borrow = 00H` | `CY`, `Z` |
| **C(1)** | 8-bit Multiplication | `4150H`, `4151H` | `05H`, `04H` | `4152H` (LSB), `4153H` (MSB) | `Product = 0014H (20D)` | `Z`, `CY` |
| **C(2)** | 8-bit Division | `4150H`, `4151H` | `14H (20D)`, `04H (4D)` | `4152H` (Quotient), `4153H` (Remainder) | `Quot = 05H, Rem = 00H` | `Z`, `CY` |
| **D(1)** | 16-bit Multiplication | `4150H-4153H` | `0100H`, `0005H` | `4154H-4157H` | `Product = 00000500H` | `Z`, `CY` |
| **D(2)** | 16-bit Division | `4150H-4153H` | `0500H`, `0100H` | `4154H-4157H` | `Quot = 0005H, Rem = 0000H` | `Z`, `CY` |

---

## ⚙️ Execution Instructions
1. Load **Microprocessor 8085 Simulator Software Kit 1.0**.
2. Open the source file from `Programs/` into the editor workspace.
3. Set base memory address to `4100H`.
4. Assemble and populate test values at `4150H` onwards.
5. Execute program (`F5`) and inspect accumulator, register pairs, and memory grid.
