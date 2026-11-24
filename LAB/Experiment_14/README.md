# Experiment 14: 8051 Data Transfer, Multi-byte Addition, Register Bank Switching and Lookup Table Programming

**Student Name:** Naga Jaswanth  
**Register Number:** 192424300  
**Course Code:** ECA1011 — Microprocessors and Microcontrollers  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences  
**Lab Date:** 21/11/26  
**Status:** `Completed & Verified ✅`

---

## 📌 Experiment Overview
This laboratory module explores data movement, memory architecture boundaries, multi-byte arithmetic, and program code-memory lookups on the **Intel 8051 Microcontroller**. Key concepts include bridging internal RAM and external RAM using the 16-bit Data Pointer (`DPTR`) with `MOVX`, carry-chain multi-byte addition (`ADDC`), register bank switching across Banks 0–3 via `PSW.3` (`RS0`) and `PSW.4` (`RS1`), stack pointer (`SP`) manipulation with `PUSH`/`POP`, and constant lookup tables in ROM using indexed addressing `MOVC A, @A+DPTR`.

---

## 📂 Directory Contents

| Folder | Description | Key Files |
|:---|:---|:---|
| **`Programs/`** | 8051 Assembly source programs (`.asm`) | `ProgA_8051_Block_Transfer.asm`, `ProgB_8051_4Byte_Addition.asm`, `ProgC_8051_Banks_Stack_MOVC.asm` |
| **`Evidence/`** | Keil μVision simulation captures | `Exp14_ProgA_8051_Block_Transfer.png`, `Exp14_ProgB_8051_4Byte_Addition.png`, `Exp14_ProgC_8051_Banks_Stack_MOVC.png` |
| **`Reports/`** | Formatted submission lab report | `Experiment_14_Report.docx` |

---

## 🔬 Program Index & Key Technical Highlights

### 1. `ProgA_8051_Block_Transfer.asm` (External RAM to Internal RAM Block Transfer)
- **Source:** External RAM `4000H`–`4004H` (`[11H, 22H, 33H, 44H, 55H]`) accessed via `MOVX A, @DPTR`.
- **Destination:** Internal RAM `50H`–`54H` accessed via `@R0`.
- **Counter:** Block length $N = 5$ managed by `R2` and `DJNZ`.

### 2. `ProgB_8051_4Byte_Addition.asm` (4-Byte Addition with Result in External RAM)
- **Operands:** Two 4-byte integers stored in Internal RAM at `40H-43H` and `50H-53H`.
- **Arithmetic:** `ADDC A, @R1` executes byte-by-byte with carry propagation.
- **Output:** 5-byte extended result written to External RAM `4500H`–`4504H` via `MOVX @DPTR, A`.

### 3. `ProgC_8051_Banks_Stack_MOVC.asm` (Register Banks, Stack & MOVC Table Lookup)
- **Register Bank Selection:**
  - Setting `PSW = 08H` selects **Bank 1** (`R0` at RAM `08H`, `R1` at RAM `09H`).
  - Setting `PSW = 00H` selects **Bank 0** (`R0` at RAM `00H`).
- **Stack Operations:**
  - Stack pointer initialized to `2FH`.
  - Direct stack pushes and pops (`PUSH 08H`, `POP 08H`) verify LIFO stack behavior.
- **Code Memory Table Lookup:**
  - `DPTR` points to `TABLE: DB 00H, 01H, 04H, 09H, 10H, 19H, 24H, 31H, 40H, 51H`.
  - `MOVC A, @A+DPTR` retrieves square values of indices `0..3` and stores them at Internal RAM `60H`–`63H`.
