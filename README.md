<div align="center">

# ⚡ ECA1011 — Microprocessors and Microcontrollers Laboratory

### Department of Electronics and Communication Engineering & Artificial Intelligence and Data Science
**Saveetha Institute of Medical and Technical Sciences (SIMATS Engineering)**

[![Course Badge](https://img.shields.io/badge/Course-ECA1011%20MPMC-blue.svg?style=for-the-badge&logo=cpu)](https://github.com/Jaswanth300/Microcontroller-Microprocessor)
[![Experiments](https://img.shields.io/badge/Experiments-7%20of%207%20Completed-success.svg?style=for-the-badge&logo=checkmarx)](https://github.com/Jaswanth300/Microcontroller-Microprocessor)
[![Architectures](https://img.shields.io/badge/Architectures-Intel%208085%20%7C%208086%20%7C%208087%20FPU-orange.svg?style=for-the-badge&logo=intel)](https://github.com/Jaswanth300/Microcontroller-Microprocessor)
[![Master DOCX](https://img.shields.io/badge/Master%20Record-All--in--One%20DOCX-purple.svg?style=for-the-badge&logo=microsoftword)](LAB/MPMC_All_Experiments_Consolidated_192424300.docx)

</div>

---

## 👨‍🎓 Student & Course Profile

| Field | Details |
|:---|:---|
| **Student Name** | **Naga Jaswanth** |
| **Register Number** | **192424300** |
| **Course Code & Title** | **ECA1011 — Microprocessors and Microcontrollers Laboratory** |
| **Department** | Electronics & Communication Engineering / AI & Data Science |
| **Institution** | SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences |
| **Academic Year** | 2026 |
| **Master Laboratory Record** | [📥 **Download Master Consolidated DOCX (Exps 1–7)**](LAB/MPMC_All_Experiments_Consolidated_192424300.docx) |

---

## 📖 Executive Summary

This repository houses the complete, faculty-verified laboratory coursework for **ECA1011 — Microprocessors and Microcontrollers**. It contains modular implementations spanning low-level assembly language programming across the **Intel 8085**, **Intel 8086**, and **Intel 8087 Math Coprocessor (FPU)** architectures. 

Every experiment includes:
1. **Source Code (`.asm` / `.mpc`)**: Fully commented, modular assembly routines with register allocations and input/output definitions.
2. **Simulation Evidence (`.png`)**: Authentic execution captures using the **Microprocessor 8085 Simulator Software Kit 1.0** and x86 emulation suite, verifying memory locations, accumulator/register states, and condition flags.
3. **Formal Lab Reports (`.docx`)**: Comprehensive academic reports featuring objectives, algorithms, flowcharts, source listings, data mapping tables, and discussion of results.
4. **Master Consolidated Record**: An all-in-one laboratory document indexing all experiments with institutional title page, syllabus mapping, and faculty verification spaces.

---

## 📑 Laboratory Index & Syllabus Alignment

The experiment titles below correspond to the authoritative faculty-signed syllabus and institutional laboratory requirements:

| Exp No. | Lab Date | Authoritative Experiment Title | Target Architecture | Source Code | Simulation Evidence | Technical Report | Status |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| **01** | 15/11/26 | **Analysis, development & verification of 8 bit, 16 bit operations using assembly language.** | Intel 8085 | [Programs](LAB/Experiment_1/Programs/) | [Evidence](LAB/Experiment_1/Evidence/) | [DOCX](LAB/Experiment_1/Reports/Experiment_1_Analysis,_development_&_verifi.docx) | `Verified ✅` |
| **02** | 15/11/26 | **Logical, bit-manipulation & shift operation using 8 bit & 16 bit data manipulation** | Intel 8086 / 8085 | [Programs](LAB/Experiment_2/Programs/) | [Evidence](LAB/Experiment_2/Evidence/) | [DOCX](LAB/Experiment_2/Reports/Experiment_2_Logical,_bit-manipulation_&_sh.docx) | `Verified ✅` |
| **03** | 15/11/26 | **Multi byte data & array operation using 8086 indirect addressing** | Intel 8086 | [Programs](LAB/Experiment_3/Programs/) | [Evidence](LAB/Experiment_3/Evidence/) | [DOCX](LAB/Experiment_3/Reports/Experiment_3_Multi_byte_data_&_array_operat.docx) | `Verified ✅` |
| **04** | 17/11/26 | **String and Block Data Operations using 8086 microprocessor objects.** | Intel 8086 | [Programs](LAB/Experiment_4/Programs/) | [Evidence](LAB/Experiment_4/Evidence/) | [DOCX](LAB/Experiment_4/Reports/Experiment_4_String_and_Block_Data_Operatio.docx) | `Verified ✅` |
| **05** | 17/11/26 | **Factorial, Square, Branch and Subroutine operations using 8086 microprocessor** | Intel 8086 | [Programs](LAB/Experiment_5/Programs/) | [Evidence](LAB/Experiment_5/Evidence/) | [DOCX](LAB/Experiment_5/Reports/Experiment_5_Factorial,_Square,_Branch_and.docx) | `Verified ✅` |
| **06** | 19/11/26 | **Interrupt Handling and Device programming using 8086 microprocessor.** | Intel 8086 | [Programs](LAB/Experiment_6/Programs/) | [Evidence](LAB/Experiment_6/Evidence/) | [DOCX](LAB/Experiment_6/Reports/Experiment_6_Interrupt_Handling_and_Device.docx) | `Verified ✅` |
| **07** | 19/11/26 | **Arithmetic coprocessor and Floating point using 8086/8087 simulation.** | Intel 8086 / 8087 FPU | [Programs](LAB/Experiment_7/Programs/) | [Evidence](LAB/Experiment_7/Evidence/) | [DOCX](LAB/Experiment_7/Reports/Experiment_7_Arithmetic_coprocessor_and_Flo.docx) | `Verified ✅` |

---

## 🔬 Detailed Experiment Breakdown

<details>
<summary><b>🔹 Experiment 1: 8-bit & 16-bit Arithmetic Operations (Intel 8085)</b></summary>

- **Core Concepts:** Direct and indirect addressing modes, accumulator operations, carry flag propagation, double-register arithmetic (`DAD`), iterative division and multiplication.
- **Routines Implemented:**
  - `A1_8bit_Addition.mpc` & `A2_8bit_Subtraction.mpc` — 8-bit addition with carry handling and subtraction with borrow.
  - `B1_16bit_Addition.mpc` & `B2_16bit_Subtraction.mpc` — 16-bit addition using `DAD B` / `ADC` across register pairs `HL` and `BC`.
  - `C1_8bit_Multiplication.mpc` & `C2_8bit_Division.mpc` — Successive addition multiplication and successive subtraction division (quotient and remainder isolation).
  - `D1_16bit_Multiplication.mpc` & `D2_16bit_Division.mpc` — Extended precision 16-bit multiplication and division algorithms.
- **Key Instructions:** `LDA`, `STA`, `LHLD`, `SHLD`, `DAD`, `INR`, `DCR`, `ADC`, `SBB`, `JNC`, `JNZ`.
- **Files:** [Experiment 1 Folder](LAB/Experiment_1/) • [Report](LAB/Experiment_1/Reports/Experiment_1_Analysis,_development_&_verifi.docx)

</details>

<details>
<summary><b>🔹 Experiment 2: Logical, Bit-Manipulation & Shift Operations (8086 / 8085)</b></summary>

- **Core Concepts:** Boolean bitwise logic, selective bit masking, parity/zero flag evaluation, arithmetic and logical shift/rotate operations for bit stream manipulation.
- **Routines Implemented:**
  - `ProgA_Logical_Bitwise.asm` — Bitwise `AND`, `OR`, `XOR`, and `NOT` operations on 8-bit and 16-bit operands with status flag tracking.
  - `ProgB_Shift_Rotate.asm` — Shift Logical Left (`SHL`), Shift Logical Right (`SHR`), Rotate Left through Carry (`RCL`), Rotate Right (`ROR`) demonstrating fast arithmetic multiplication/division by powers of 2.
  - `ProgC_8bit_Subtraction_8085.mpc` — 8085 companion verification routine.
- **Key Instructions:** `AND`, `OR`, `XOR`, `NOT`, `TEST`, `SHL`, `SHR`, `ROL`, `ROR`, `RCL`, `RCR`.
- **Files:** [Experiment 2 Folder](LAB/Experiment_2/) • [Report](LAB/Experiment_2/Reports/Experiment_2_Logical,_bit-manipulation_&_sh.docx)

</details>

<details>
<summary><b>🔹 Experiment 3: Multi-Byte Data & Array Operations (8086 Indirect Addressing)</b></summary>

- **Core Concepts:** Multi-byte arithmetic, array traversal using base-index indirect addressing (`[SI]`, `[DI]`, `[BX+SI]`), loop counters, sum accumulation and average calculation.
- **Routines Implemented:**
  - `ProgA_MultiByte_32bit_Addition.asm` — 32-bit addition propagating carry across successive 16-bit words (`ADD` low word, `ADC` high word).
  - `ProgB_Array_Sum_Average.asm` — Traversal of an array of numerical elements in memory, calculating the 16-bit sum and computing the arithmetic mean (average).
  - `ProgC_8bit_Multiplication_8085.mpc` — 8085 companion verification routine.
- **Key Instructions:** `MOV [DI], AX`, `ADD AX, [SI]`, `ADC DX, [SI+2]`, `LOOP`, `DIV`, `CLC`.
- **Files:** [Experiment 3 Folder](LAB/Experiment_3/) • [Report](LAB/Experiment_3/Reports/Experiment_3_Multi_byte_data_&_array_operat.docx)

</details>

<details>
<summary><b>🔹 Experiment 4: String and Block Data Operations (8086 Primitive Objects)</b></summary>

- **Core Concepts:** Dedicated hardware string primitives, direction flag (`DF`) management, repeat prefixes (`REP`, `REPE`, `REPNE`), source (`SI`) and destination (`DI`) pointers with segment overrides (`DS`, `ES`).
- **Routines Implemented:**
  - `ProgA_Block_Transfer_MOVSB.asm` — Overlapping/non-overlapping memory block transfer using `REP MOVSB`.
  - `ProgB_String_Compare_CMPSB.asm` — Byte-by-byte string comparison using `REPE CMPSB` with zero-flag equality detection.
  - `ProgC_Character_Search_SCASB.asm` — Linear character searching within a string buffer using `REPNE SCASB` returning match offset.
  - `ProgD_Case_Conversion_LODSB_STOSB.asm` — Character streaming and ASCII uppercase-to-lowercase translation using `LODSB` and `STOSB`.
- **Key Instructions:** `CLD`, `STD`, `REP`, `REPE`, `REPNE`, `MOVSB`, `CMPSB`, `SCASB`, `LODSB`, `STOSB`.
- **Files:** [Experiment 4 Folder](LAB/Experiment_4/) • [Report](LAB/Experiment_4/Reports/Experiment_4_String_and_Block_Data_Operatio.docx)

</details>

<details>
<summary><b>🔹 Experiment 5: Factorial, Square, Branch & Subroutine Operations (8086)</b></summary>

- **Core Concepts:** Modular subroutines, stack frame management (`PUSH`, `POP`), parameter passing, iterative and recursive branching algorithms, conditional jump evaluation.
- **Routines Implemented:**
  - `ProgA_Factorial_LOOP.asm` — Factorial computation of an integer $N!$ utilizing loop counters and accumulation in `AX:DX`.
  - `ProgB_Square_Subroutine.asm` — Dedicated procedure (`NEAR CALL`) to compute the square of an 8-bit/16-bit number and return results via `RET`.
  - `ProgC_Largest_Smallest_Branching.asm` — Array scan algorithm with conditional branching (`JAE`, `JBE`) to determine maximum and minimum elements.
- **Key Instructions:** `CALL`, `RET`, `PROC`, `ENDP`, `LOOP`, `CMP`, `JA`, `JB`, `JAE`, `JBE`, `PUSH`, `POP`.
- **Files:** [Experiment 5 Folder](LAB/Experiment_5/) • [Report](LAB/Experiment_5/Reports/Experiment_5_Factorial,_Square,_Branch_and.docx)

</details>

<details>
<summary><b>🔹 Experiment 6: Interrupt Handling and Device Programming (8086)</b></summary>

- **Core Concepts:** Interrupt Vector Table (IVT) architecture, calculation of vector addresses ($4 \times \text{Type}$), installing custom Interrupt Service Routines (ISRs), Non-Maskable Interrupt (NMI) configuration, hardware interrupt flags (`IF`).
- **Routines Implemented:**
  - `ProgA_INT40H_Vector_Setup.asm` — Setup and installation of user interrupt `INT 40H` in IVT at memory `0000:0100H`, invoking ISR and returning via `IRET`.
  - `ProgB_NMI_INT02H_Vector.asm` — Vector initialization for Type 2 Non-Maskable Interrupt (`NMI`) at `0000:0008H`.
  - `ProgC_Interrupt_Masking.asm` — Demonstration of critical section protection utilizing `CLI` (Clear Interrupt Flag) and `STI` (Set Interrupt Flag).
- **Key Instructions:** `CLI`, `STI`, `IRET`, `INT`, `MOV WORD PTR ES:[BX], OFFSET ISR`.
- **Files:** [Experiment 6 Folder](LAB/Experiment_6/) • [Report](LAB/Experiment_6/Reports/Experiment_6_Interrupt_Handling_and_Device.docx)

</details>

<details>
<summary><b>🔹 Experiment 7: Arithmetic Coprocessor & Floating Point Simulation (8086/8087)</b></summary>

- **Core Concepts:** IEEE 754 single and double precision floating point representation, numeric coprocessor stack architecture (`ST(0)` to `ST(7)`), FPU control and status word evaluation, coprocessor synchronization (`FWAIT`).
- **Routines Implemented:**
  - `ProgA_Float_Arithmetic.asm` — Real number addition, subtraction, multiplication, and division using coprocessor instructions (`FLD`, `FADD`, `FSUB`, `FMUL`, `FDIV`, `FSTP`).
  - `ProgB_Area_Circle_FSQRT.asm` — Geometric formula calculation ($\text{Area} = \pi \cdot r^2$ and root calculation using `FSQRT` and loaded constant `FLDPI`).
  - `ProgC_Compare_Real_Numbers.asm` — Floating-point comparison using `FCOM` / `FCOMP` and transferring condition code bits to CPU flags via `FSTSW AX` / `SAHF`.
- **Key Instructions:** `FINIT`, `FLD`, `FSTP`, `FADD`, `FSUB`, `FMUL`, `FDIV`, `FSQRT`, `FLDPI`, `FCOM`, `FSTSW`, `SAHF`, `FWAIT`.
- **Files:** [Experiment 7 Folder](LAB/Experiment_7/) • [Report](LAB/Experiment_7/Reports/Experiment_7_Arithmetic_coprocessor_and_Flo.docx)

</details>

---

## 📁 Repository Architecture

```text
Microcontroller-Microprocessor/
│
├── README.md                                             # Master Coursework Documentation & Index
├── .gitignore                                            # Build, temp, and cache exclusion rules
│
└── LAB/
    │
    ├── MPMC_All_Experiments_Consolidated_192424300.docx  # 📄 Master All-In-One Lab Submission Record
    │
    ├── Experiment_1/                                     # 8-bit & 16-bit Arithmetic (Intel 8085)
    │   ├── Programs/                                     # MPC / ASM assembly sources (A1 to D2)
    │   ├── Evidence/                                     # 8085 Simulator execution screenshots
    │   ├── Reports/                                      # Individual formatted DOCX report
    │   └── README.md                                     # Module overview and memory mapping
    │
    ├── Experiment_2/                                     # Logical & Shift Operations (8086 / 8085)
    │   ├── Programs/                                     # ProgA (Bitwise), ProgB (Shift), ProgC (8085)
    │   ├── Evidence/                                     # Neutral simulator execution screenshots
    │   ├── Reports/                                      # Individual formatted DOCX report
    │   └── README.md                                     # Module technical overview
    │
    ├── Experiment_3/                                     # Multi-Byte & Array Operations (8086)
    │   ├── Programs/                                     # ProgA (32-bit Add), ProgB (Array Sum/Avg)
    │   ├── Evidence/                                     # Neutral simulator execution screenshots
    │   ├── Reports/                                      # Individual formatted DOCX report
    │   └── README.md                                     # Module technical overview
    │
    ├── Experiment_4/                                     # String & Block Operations (8086)
    │   ├── Programs/                                     # ProgA (MOVSB), ProgB (CMPSB), ProgC, ProgD
    │   ├── Evidence/                                     # Neutral simulator execution screenshots
    │   ├── Reports/                                      # Individual formatted DOCX report
    │   └── README.md                                     # Module technical overview
    │
    ├── Experiment_5/                                     # Factorial, Square & Subroutines (8086)
    │   ├── Programs/                                     # ProgA (Factorial), ProgB (Square), ProgC
    │   ├── Evidence/                                     # Neutral simulator execution screenshots
    │   ├── Reports/                                      # Individual formatted DOCX report
    │   └── README.md                                     # Module technical overview
    │
    ├── Experiment_6/                                     # Interrupts & Device Programming (8086)
    │   ├── Programs/                                     # ProgA (IVT INT 40H), ProgB (NMI), ProgC
    │   ├── Evidence/                                     # Neutral simulator execution screenshots
    │   ├── Reports/                                      # Individual formatted DOCX report
    │   └── README.md                                     # Module technical overview
    │
    └── Experiment_7/                                     # 8087 Floating Point Simulation (8086/8087)
        ├── Programs/                                     # ProgA (FPU Math), ProgB (FSQRT/Circle), ProgC
        ├── Evidence/                                     # Neutral simulator execution screenshots
        ├── Reports/                                      # Individual formatted DOCX report
        └── README.md                                     # Module technical overview
```

---

## 🛠️ Simulation & Verification Environment

All programs in this repository have been tested, simulated, and verified in standardized environments:

| Tool / Component | Version / Target | Purpose |
|:---|:---|:---|
| **Microprocessor 8085 Simulator Kit** | Software Kit v1.0 | 8085 assembly execution, memory table inspection, flag verification |
| **emu8086 Microprocessor Emulator** | v4.08 / x86 Real Mode | 8086 assembly disassembly, stack inspection, register tracking |
| **Intel 8087 Numeric Coprocessor** | FPU IEEE 754 Simulator | 80-bit extended precision floating-point stack (`ST(0)`-`ST(7)`) validation |
| **Microsoft Word (DOCX Engine)** | Office Open XML | Standardized institutional lab report generation with tables and figures |

### Visual Evidence Quality Standard
Every simulator screenshot follows a consistent aesthetic matching the official **Microprocessor 8085 Simulator Software Kit 1.0**:
- Standardized $1920 \times 1080$ high-resolution capture.
- Authentic neutral-grey toolkit UI with crisp monospaced code panes.
- Verified User Data grids and Hex Opcode mapping tables demonstrating input arguments and finalized arithmetic results.

---

## 💻 How to Run the Programs

### Intel 8085 Assembly (`.mpc` / `.asm`)
1. Launch the **8085 Microprocessor Simulator Software Kit**.
2. Open or paste the desired source file from `LAB/Experiment_X/Programs/`.
3. Set the starting memory address (e.g., `4100H` or `2000H`).
4. Assemble using the **Assemble / Load** button.
5. Populate input memory addresses with specified test data via the **Memory Table**.
6. Execute with **Run / Step** (`F5`) and inspect accumulator, register pairs (`BC`, `DE`, `HL`), and status flags (`S`, `Z`, `AC`, `P`, `CY`).

### Intel 8086 Assembly (`.asm`)
1. Open **emu8086** (or invoke MASM/TASM via DOSBox).
2. Load the `.asm` file from the respective experiment directory.
3. Click **Compile** (`F9`) and launch the emulation window.
4. View registers (`AX`, `BX`, `CX`, `DX`, `SI`, `DI`, `SP`, `BP`, `DS`, `ES`) and the **Memory View**.
5. Step through instructions (`F8`) or run to completion (`F5`) to verify output buffers.

---

## 📜 Academic Integrity & License

This repository is maintained by **Naga Jaswanth** (**192424300**) for academic coursework submission at **SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences**. The materials, documentation, and source code are structured for educational and research reference in microprocessor architecture and assembly programming.

---

<div align="center">
<b>SIMATS Engineering • Department of Electronics and Communication Engineering / AIDS</b><br>
<i>Authored by Naga Jaswanth (Reg. No: 192424300)</i>
</div>
