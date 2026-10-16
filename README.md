# Microprocessors and Microcontrollers (MPMC) Laboratory

This repository contains academic coursework, assembly language implementations, simulation evidence, automated validation suites, and laboratory reports for the **Microprocessors and Microcontrollers (MPMC)** course.

## Course Information
* **Subject**: Microprocessors and Microcontrollers (MPMC)
* **Author / Student**: Jaswanth (`Jaswanth300`)
* **Target Architectures**: Intel 8085 (8-bit) & Intel 8086 (16-bit)

---

## Repository Structure

```text
MPMC/
├── .gitignore                                # Coursework ignore configuration
├── README.md                                 # Top-level course overview
├── 8085/                                     # Intel 8085 sample assembly programs (.mpc)
│   ├── 01Sample.mpc ... 11Sample.mpc
│   └── FGMJJHJKL.mpc
├── 8086/                                     # Intel 8086 assembly coursework
│   └── FACTORIAL OF A NUMBER.docx
└── LAB/                                      # Laboratory Experiments
    ├── Experiment_1_8085_Arithmetic_Operations_Final.docx  # Final Experiment 1 Report
    ├── Experiment_1_8085_Arithmetic_Operations_Draft.docx  # Baseline draft report
    ├── 8085-16_bit_Multiplication.mpc        # 16-bit multiplication prototype
    ├── 8085-16_bit_Division.mpc              # 16-bit division prototype
    ├── B(1) — 16-bit Addition.mpc            # 16-bit addition program (4200H)
    ├── B(1) — 16-bit Subtraction.mpc         # 16-bit subtraction program (4200H)
    ├── D(1) — 16-bit Multiplication.mpc     # 16-bit multiplication program (4400H)
    ├── D(2) — 16-bit Division.mpc           # 16-bit division program (442DH)
    └── Experiment_1/                         # Structured Experiment 1 Deliverables
        ├── Evidence/                         # Genuine simulator execution screenshots
        ├── Logs/                             # Integrity manifests & validation summaries
        ├── Programs/                         # All 8 verified .mpc programs (A1–D2)
        ├── Reports/                          # Final DOCX report
        ├── Scripts/                          # Safe CLI automation & validation utilities
        └── README.md                         # Detailed Experiment 1 documentation
```

---

## Experiments

### Experiment 1: 8-Bit and 16-Bit Arithmetic Operations (Intel 8085)
Complete development, simulation, verification, and documentation of all eight arithmetic modules:
* **Section A (4100H)**: 8-Bit Addition & Subtraction with carry, borrow, and PSW flag register storage.
* **Section B (4200H)**: 16-Bit Addition & Subtraction with carry and borrow verification.
* **Section C (4300H)**: 8-Bit Multiplication (repeated addition) & Division (repeated subtraction).
* **Section D (4400H / 442DH)**: 16-Bit Multiplication (32-bit product) & 16-Bit Division.

See [LAB/Experiment_1/README.md](LAB/Experiment_1/README.md) for full instructions, memory tables, and verification commands.
