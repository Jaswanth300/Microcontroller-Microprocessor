# Experiment 2: Logical, bit-manipulation & shift operation using 8 bit & 16 bit data manipulation

**Student Name:** Naga Jaswanth  
**Register Number:** 192424300  
**Course Code:** ECA1011 — Microprocessors and Microcontrollers  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences  
**Lab Date:** 15/11/26  
**Status:** `Completed & Verified ✅`

---

## 📌 Experiment Overview
This laboratory module investigates logical operations, selective bit-masking, and bit-level shift/rotate mechanisms on the **Intel 8086 Microprocessor** (with companion 8085 verification). The experiment reinforces understanding of bitwise boolean logic (`AND`, `OR`, `XOR`, `NOT`) and binary positional shifts (`SHL`, `SHR`, `ROL`, `ROR`, `RCL`, `RCR`).

---

## 📂 Directory Contents

| Folder | Description | Key Files |
|:---|:---|:---|
| **`Programs/`** | Assembly source programs (`.asm` / `.mpc`) | `ProgA_Logical_Bitwise.asm`, `ProgB_Shift_Rotate.asm`, `ProgC_8bit_Subtraction_8085.mpc` |
| **`Evidence/`** | Standardized simulator execution captures | `Exp2_ProgA_Logical_Bit_Manipulation.png`, `Exp2_ProgB_Shift_Rotate_Operations.png`, `Exp2_ProgC_8bit_Subtraction_8085.png` |
| **`Reports/`** | Formatted submission lab report | `Experiment_2_Logical,_bit-manipulation_&_sh.docx` |

---

## 🔬 Program Index & Key Technical Highlights

### 1. `ProgA_Logical_Bitwise.asm`
- **Operands:** `DATA1 = 0FH (0000 1111B)`, `DATA2 = 33H (0011 0011B)`
- **Operations:**
  - `AND`: `0FH AND 33H = 03H` (Bit masking)
  - `OR`: `0FH OR 33H = 3FH` (Bit setting)
  - `XOR`: `0FH XOR 33H = 3CH` (Bit toggling / difference detection)
  - `NOT`: `NOT 0FH = F0H` (1's complement inversion)
- **Status Flags:** `ZF` (Zero), `SF` (Sign), `PF` (Parity).

### 2. `ProgB_Shift_Rotate.asm`
- **Operand:** `DATA = A5H (1010 0101B)`
- **Operations:**
  - `SHL AL, 1` $\rightarrow$ Fast multiplication by 2 (`4AH`, `CF = 1`)
  - `SHR AL, 1` $\rightarrow$ Logical division by 2 (`52H`, `CF = 1`)
  - `ROL AL, 1` $\rightarrow$ Circular left rotation (`4BH`, `CF = 1`)
  - `ROR AL, 1` $\rightarrow$ Circular right rotation (`D2H`, `CF = 1`)

### 3. `ProgC_8bit_Subtraction_8085.mpc`
- **Operands:** `4150H = 36H`, `4151H = 12H` $\rightarrow$ `Difference = 24H` at `4152H`.
