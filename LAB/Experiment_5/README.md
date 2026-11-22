# Experiment 5: Factorial, Square, Branch and Subroutine operations using 8086 microprocessor

**Student Name:** Naga Jaswanth  
**Register Number:** 192424300  
**Course Code:** ECA1011 — Microprocessors and Microcontrollers  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences  
**Lab Date:** 17/11/26  
**Status:** `Completed & Verified ✅`

---

## 📌 Experiment Overview
This laboratory module investigates control transfer, stack frame operations, modular subroutine organization (`CALL` / `RET`), and multi-way conditional branching on the **Intel 8086 Microprocessor**. The focus is on implementing iterative/recursive mathematical calculations (Factorial), modular procedure linkage (Squaring subroutines), and comparative array sorting/scanning (Largest & Smallest detection).

---

## 📂 Directory Contents

| Folder | Description | Key Files |
|:---|:---|:---|
| **`Programs/`** | Assembly source programs (`.asm`) | `ProgA_Factorial_LOOP.asm`, `ProgB_Square_Subroutine.asm`, `ProgC_Largest_Smallest_Branching.asm` |
| **`Evidence/`** | Standardized simulator execution captures | `Exp5_ProgA_Factorial_LOOP.png`, `Exp5_ProgB_Square_Subroutine.png`, `Exp5_ProgC_Largest_Smallest_Branching.png` |
| **`Reports/`** | Formatted submission lab report | `Experiment_5_Factorial,_Square,_Branch_and.docx` |

---

## 🔬 Program Index & Key Technical Highlights

### 1. `ProgA_Factorial_LOOP.asm`
- **Objective:** Compute $N!$ for $N = 5$.
- **Algorithm:** Initialize accumulator `AX = 0001H`, counter `CX = 0005H`. Multiply `AX` by `CX` and decrement `CX` with `LOOP FACT_LOOP` until `CX = 0`.
- **Result:** $5! = 120\text{D} = 0078\text{H}$ stored in `AX`.

### 2. `ProgB_Square_Subroutine.asm`
- **Objective:** Implement modular subroutine `SQUARE_PROC` called via `CALL NEAR`.
- **Mechanism:** Parameter $N = 12\text{D} (0\text{CH})$ passed via `AL`. Procedure executes `MUL AL`, stores 16-bit result (`144\text{D} = 0090\text{H}`) in `AX`, pops return address off stack, and resumes caller via `RET`.
- **Stack Verification:** Stack pointer `SP` decrements by 2 on `CALL` and increments by 2 on `RET`.

### 3. `ProgC_Largest_Smallest_Branching.asm`
- **Objective:** Scan an array of 5 unsigned numbers (`[25H, 80H, 12H, 9AH, 45H]`) and isolate the maximum and minimum values.
- **Branching Instructions:** `CMP AL, [SI]`, `JAE NOT_GREATER`, `JBE NOT_SMALLER`.
- **Result:** `LARGEST = 9AH (154D)`, `SMALLEST = 12H (18D)`.
