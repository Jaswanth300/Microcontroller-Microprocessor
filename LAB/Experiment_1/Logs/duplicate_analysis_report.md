# Experiment 1: MPC Program Analysis & Duplicate Evaluation Report

## 1. Executive Summary

A deep structural and assembly inspection of all `.mpc` files in the repository was conducted. No files should be deleted. The generic-named programs (`8085-16_bit_*.mpc`) are distinct prototypes, while the specifically-named programs (`B(1)...`, `D(1)...`, `D(2)...`) strictly implement the authoritative Experiment 1 memory map and starting addresses.

## 2. Program Comparison Matrix

| Program File | Start Address | Input Addresses | Output Addresses | Status / Role |
| :--- | :--- | :--- | :--- | :--- |
| `8085-16_bit_Division.mpc` | `8000H` | `2050 - 2055` | See UserData Grid | Generic Prototype |
| `8085-16_bit_Multiplication.mpc` | `0000H` | `2050 - 2057` | See UserData Grid | Generic Prototype |
| `B(1) — 16-bit Addition.mpc` | `4200H` | `4510 - 4519` | See UserData Grid | Authoritative Lab Program |
| `B(1) — 16-bit Subtraction.mpc` | `4200H` | `4510 - 451A` | See UserData Grid | Authoritative Lab Program |
| `D(1) — 16-bit Multiplication.mpc` | `4400H` | `4530 - 4537` | See UserData Grid | Authoritative Lab Program |
| `D(2) — 16-bit Division.mpc` | `442DH` | `4538 - 453F` | See UserData Grid | Authoritative Lab Program |

## 3. Detailed Program Comparison

### 16-bit Multiplication

- **Generic File**: `8085-16_bit_Multiplication.mpc`
  - Start Address: `0000H`
  - Memory Region: `2050H - 2053H`
- **Authoritative File**: `D(1) — 16-bit Multiplication.mpc`
  - Start Address: `4400H` (Complies with Section 6 & 7)
  - Input Memory: `4530H - 4533H (Inputs: 34H, 12H, 78H, 56H -> X=1234H, Y=5678H)`
  - Output Memory: `4534H - 4537H (Outputs: 60H, 00H, 26H, 06H -> 06260060H)`
- **Conclusion**: Preserve both. Use D(1) as the authoritative Experiment 1 lab submission.

### 16-bit Division

- **Generic File**: `8085-16_bit_Division.mpc`
  - Start Address: `8000H`
  - Memory Region: `2050H - 2053H (Sample test data: 5AH, 01H, 0CH, 00H)`
- **Authoritative File**: `D(2) — 16-bit Division.mpc`
  - Start Address: `442DH` (Complies with Section 6 & 7)
  - Input Memory: `4538H - 453BH (Inputs: 78H, 56H, 34H, 12H -> Dividend=5678H, Divisor=1234H)`
  - Output Memory: `453CH - 453FH (Quotient: 04H, 00H; Remainder: A8H, 0DH)`
- **Conclusion**: Preserve both. Use D(2) as the authoritative Experiment 1 lab submission.

