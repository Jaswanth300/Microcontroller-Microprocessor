# Experiment 3: Multi byte data & array operation using 8086 indirect addressing

**Student Name:** Naga Jaswanth  
**Register Number:** 192424300  
**Course Code:** ECA1011 — Microprocessors and Microcontrollers  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences  
**Lab Date:** 15/11/26  
**Status:** `Completed & Verified ✅`

---

## 📌 Experiment Overview
This laboratory module explores multi-byte arithmetic expansion and linear array processing using the **Intel 8086 Microprocessor**. Key objectives include handling operand sizes beyond standard 16-bit register limits using carry-chain arithmetic (`ADC`), and utilizing pointer-based indirect addressing modes (`[SI]`, `[DI]`, `[BX+SI]`) to traverse arrays, accumulate sums, and compute statistical averages.

---

## 📂 Directory Contents

| Folder | Description | Key Files |
|:---|:---|:---|
| **`Programs/`** | Assembly source programs (`.asm` / `.mpc`) | `ProgA_MultiByte_32bit_Addition.asm`, `ProgB_Array_Sum_Average.asm`, `ProgC_8bit_Multiplication_8085.mpc` |
| **`Evidence/`** | Standardized simulator execution captures | `Exp3_ProgA_MultiByte_32bit_Addition.png`, `Exp3_ProgB_Array_Sum_Average.png`, `Exp3_ProgC_8bit_Multiplication_8085.png` |
| **`Reports/`** | Formatted submission lab report | `Experiment_3_Multi_byte_data_&_array_operat.docx` |

---

## 🔬 Program Index & Key Technical Highlights

### 1. `ProgA_MultiByte_32bit_Addition.asm`
- **Operands:** 
  - Number 1: `12345678H` (Low Word: `5678H`, High Word: `1234H`)
  - Number 2: `87654321H` (Low Word: `4321H`, High Word: `8765H`)
- **Execution:**
  - `ADD AX, BX` on low words (`5678H + 4321H = 9999H`, `CF = 0`)
  - `ADC CX, DX` on high words (`1234H + 8765H + CF = 9999H`)
- **Result:** `99999999H` with `CF = 0`.

### 2. `ProgB_Array_Sum_Average.asm`
- **Dataset:** 5 elements: `[10H, 20H, 30H, 40H, 50H]` (Array Count: `05H`)
- **Execution:**
  - Pointer `SI` initialized to base of array.
  - Counter `CX` loaded with `0005H`.
  - Accumulator `AX` sums elements: `10H + 20H + 30H + 40H + 50H = 00F0H (240D)`.
  - Average computed via `DIV BL`: `F0H / 05H = 30H (48D)` with remainder `00H`.
- **Result:** Sum = `00F0H`, Average = `30H`, Remainder = `00H`.

### 3. `ProgC_8bit_Multiplication_8085.mpc`
- **Operands:** `4150H = 05H`, `4151H = 04H` $\rightarrow$ Product = `0014H (20D)` at `4152H-4153H`.
