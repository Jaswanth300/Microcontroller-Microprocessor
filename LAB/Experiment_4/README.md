# Experiment 4: String and Block Data Operations using 8086 microprocessor objects.

**Student Name:** Naga Jaswanth  
**Register Number:** 192424300  
**Course Code:** ECA1011 — Microprocessors and Microcontrollers  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences  
**Lab Date:** 17/11/26  
**Status:** `Completed & Verified ✅`

---

## 📌 Experiment Overview
This laboratory module investigates the hardware string primitives of the **Intel 8086 Microprocessor**. String instructions provide single-instruction data block manipulation by leveraging auto-incrementing/decrementing index pointers (`SI` and `DI`) governed by the Direction Flag (`DF`), together with the `REP` (Repeat), `REPE` (Repeat while Equal), and `REPNE` (Repeat while Not Equal) prefixes.

---

## 📂 Directory Contents

| Folder | Description | Key Files |
|:---|:---|:---|
| **`Programs/`** | Assembly source programs (`.asm`) | `ProgA_Block_Transfer_MOVSB.asm`, `ProgB_String_Compare_CMPSB.asm`, `ProgC_Character_Search_SCASB.asm`, `ProgD_Case_Conversion_LODSB_STOSB.asm` |
| **`Evidence/`** | Standardized simulator execution captures | `Exp4_ProgA_Block_Transfer_MOVSB.png`, `Exp4_ProgB_String_Compare_CMPSB.png`, `Exp4_ProgC_Character_Search_SCASB.png`, `Exp4_ProgD_Case_Conversion_LODSB_STOSB.png` |
| **`Reports/`** | Formatted submission lab report | `Experiment_4_String_and_Block_Data_Operatio.docx` |

---

## 🔬 Program Index & Key Technical Highlights

### 1. `ProgA_Block_Transfer_MOVSB.asm`
- **Objective:** Transfer a block of $N = 10$ bytes from `SRC_BLOCK` to `DST_BLOCK`.
- **Implementation:** `CLD`, `LEA SI, SRC`, `LEA DI, DST`, `MOV CX, 10`, `REP MOVSB`.
- **Outcome:** Exact byte-for-byte replication in memory; verified via memory buffer dump.

### 2. `ProgB_String_Compare_CMPSB.asm`
- **Objective:** Compare two strings for equality using `REPE CMPSB`.
- **Test Strings:** `STR1 = "SIMATS2026"`, `STR2 = "SIMATS2026"` $\rightarrow$ Match (`FLAG = 01H`). Mismatch test evaluates `FLAG = 00H`.

### 3. `ProgC_Character_Search_SCASB.asm`
- **Objective:** Locate target character `'E'` within a string buffer using `REPNE SCASB`.
- **Outcome:** Target detected, index offset computed from remaining `CX` counter value.

### 4. `ProgD_Case_Conversion_LODSB_STOSB.asm`
- **Objective:** Stream characters from source string, translate ASCII lowercase (`61H-7AH`) to uppercase (`41H-5AH`) by subtracting `20H`, and write back to destination.
- **Key Operations:** `LODSB`, `SUB AL, 20H`, `STOSB`, `LOOP`.
