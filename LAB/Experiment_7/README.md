# Experiment 7: Arithmetic coprocessor and Floating point using 8086/8087 simulation.

**Student Name:** Naga Jaswanth  
**Register Number:** 192424300  
**Course Code:** ECA1011 — Microprocessors and Microcontrollers  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences  
**Lab Date:** 19/11/26  
**Status:** `Completed & Verified ✅`

---

## 📌 Experiment Overview
This laboratory module investigates numeric data processing using the **Intel 8087 Math Coprocessor (FPU)** tightly coupled with the **Intel 8086 Microprocessor**. The experiment covers the 80-bit extended-precision floating-point register stack (`ST(0)` through `ST(7)`), IEEE 754 single-precision (32-bit) and double-precision (64-bit) representations, arithmetic computation (`FADD`, `FSUB`, `FMUL`, `FDIV`), geometric and transcendental operations (`FSQRT`, `FLDPI`), and condition code transfer to CPU flags via `FSTSW AX` / `SAHF`.

---

## 📂 Directory Contents

| Folder | Description | Key Files |
|:---|:---|:---|
| **`Programs/`** | Assembly source programs (`.asm`) | `ProgA_Float_Arithmetic.asm`, `ProgB_Area_Circle_FSQRT.asm`, `ProgC_Compare_Real_Numbers.asm` |
| **`Evidence/`** | Standardized simulator execution captures | `Exp7_ProgA_Float_Arithmetic.png`, `Exp7_ProgB_Area_Circle_FSQRT.png` |
| **`Reports/`** | Formatted submission lab report | `Experiment_7_Arithmetic_coprocessor_and_Flo.docx` |

---

## 🔬 Program Index & Key Technical Highlights

### 1. `ProgA_Float_Arithmetic.asm`
- **Operands:** IEEE 754 32-bit single-precision floats:
  - $A = 12.5\text{D} = \text{41480000H}$
  - $B = 2.5\text{D} = \text{40200000H}$
- **Calculations:**
  - Addition: $12.5 + 2.5 = 15.0\text{D} = \text{41700000H}$
  - Subtraction: $12.5 - 2.5 = 10.0\text{D} = \text{41200000H}$
  - Multiplication: $12.5 \times 2.5 = 31.25\text{D} = \text{41FA0000H}$
  - Division: $12.5 / 2.5 = 5.0\text{D} = \text{40A00000H}$
- **Key Instructions:** `FINIT`, `FLD`, `FADD`, `FSUB`, `FMUL`, `FDIV`, `FSTP`.

### 2. `ProgB_Area_Circle_FSQRT.asm`
- **Objective:** Compute area and square root: $\text{Area} = \pi \cdot r^2$ for radius $r = 4.0\text{D}$.
- **FPU Operations:**
  - `FLD RADIUS` $\rightarrow$ Load $4.0$ to `ST(0)`
  - `FMUL ST(0), ST(0)` $\rightarrow$ Compute $r^2 = 16.0$
  - `FLDPI` $\rightarrow$ Push $\pi \approx 3.14159265$ to `ST(0)`
  - `FMULP ST(1), ST(0)` $\rightarrow$ Area $= 50.2655\text{D} = \text{42490FD0H}$
  - `FSQRT` on $16.0$ evaluates root back to $4.0$.

### 3. `ProgC_Compare_Real_Numbers.asm`
- **Objective:** Compare two floating-point values and branch conditionally in 8086 code.
- **Mechanism:** `FCOM NUM2` sets coprocessor condition flags `C0`, `C2`, `C3`. `FSTSW AX` transfers status word to accumulator, and `SAHF` loads `AH` into CPU flags (`CF`, `ZF`), allowing standard `JA`, `JB`, `JE` instructions.
