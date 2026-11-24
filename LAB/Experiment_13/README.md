# Experiment 13: 8051 Arithmetic, Logical and Bit-Manipulation Programming Using Keil

**Student Name:** Naga Jaswanth  
**Register Number:** 192424300  
**Course Code:** ECA1011 — Microprocessors and Microcontrollers  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences  
**Lab Date:** 20/11/26  
**Status:** `Completed & Verified ✅`

---

## 📌 Experiment Overview
This laboratory module investigates low-level assembly language programming for the **Intel 8051 Microcontroller** (MCS-51 architecture) within the **Keil μVision IDE**. The focus is on evaluating the 8051 ALU operations, hardware multiplier/divider (`MUL AB`, `DIV AB`), Program Status Word (`PSW`) flag behaviors (`CY`, `AC`, `OV`, `P`), boolean bit manipulation in the bit-addressable RAM region (`20H`–`2FH`), and nibble manipulation (`SWAP`).

---

## 📂 Directory Contents

| Folder | Description | Key Files |
|:---|:---|:---|
| **`Programs/`** | 8051 Assembly source programs (`.asm`) | `Prog1_8051_Add_Sub.asm`, `Prog2_8051_Mul_Div.asm`, `Prog3_8051_Logical_Bitwise.asm` |
| **`Evidence/`** | Keil μVision simulation captures | `Exp13_Prog1_8051_Add_Sub.png`, `Exp13_Prog2_8051_Mul_Div.png`, `Exp13_Prog3_8051_Logical_Bitwise.png` |
| **`Reports/`** | Formatted submission lab report | `Experiment_13_Report.docx` |

---

## 🔬 Program Index & Key Technical Highlights

### 1. `Prog1_8051_Add_Sub.asm` (8-Bit Addition and Subtraction)
- **Operands:** `RAM 30H = B5H`, `RAM 31H = 6EH`
- **Addition:** `ADD A, 31H` $\rightarrow$ `A = 23H`, `CY = 1`, `AC = 1`, `OV = 0`, `P = 0`. Stored at `RAM 32H`.
- **Subtraction:** `CLR C`, `SUBB A, 31H` $\rightarrow$ `A = 47H`, `CY = 0`, `AC = 0`, `OV = 1`, `P = 1`. Stored at `RAM 34H`.
- **Flag Registers:** Full `PSW` byte saved at `33H` and `35H`.

### 2. `Prog2_8051_Mul_Div.asm` (8-Bit Multiplication and Division)
- **Multiplication:**
  - Operands: `36H = C8H (200D)`, `37H = 0AH (10D)`
  - Instruction: `MUL AB`
  - Result: High byte in `B = 07H`, Low byte in `A = D0H` $\rightarrow$ `Product = 07D0H (2000D)` stored at `38H-39H`.
- **Division:**
  - Operands: `3AH = FFH (255D)`, `3BH = 0DH (13D)`
  - Instruction: `DIV AB`
  - Result: Quotient in `A = 13H (19D)`, Remainder in `B = 08H (8D)` stored at `3CH-3DH`.

### 3. `Prog3_8051_Logical_Bitwise.asm` (Bitwise Logic & Bit-Addressable Memory)
- **Input Operand:** `RAM 40H = A5H (1010 0101B)`
- **Logical Operations:**
  - `ORL A, #0FH` $\rightarrow$ `AFH` (stored at `41H`)
  - `ANL A, #0F0H` $\rightarrow$ `A0H` (stored at `42H`)
  - `XRL A, #0FFH` $\rightarrow$ `5AH` (stored at `43H`)
  - `SWAP A` $\rightarrow$ `5AH` (stored at `44H`)
  - `RL A` $\rightarrow$ `4BH` (stored at `45H`)
  - `RR A` $\rightarrow$ `D2H` (stored at `46H`)
- **Bit-Addressable RAM (Byte `20H`):**
  - `SETB 00H` (Bit `20.0 = 1`), `SETB 07H` (Bit `20.7 = 1`)
  - `MOV C, ACC.0`, `MOV 01H, C` (Bit `20.1 = 1`)
  - `CPL 00H` (Bit `20.0 = 0`)
  - Final byte `20H` stored at `47H`.
