# Experiment 6: Interrupt Handling and Device programming using 8086 microprocessor.

**Student Name:** Naga Jaswanth  
**Register Number:** 192424300  
**Course Code:** ECA1011 — Microprocessors and Microcontrollers  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences  
**Lab Date:** 19/11/26  
**Status:** `Completed & Verified ✅`

---

## 📌 Experiment Overview
This laboratory module investigates the interrupt architecture, Interrupt Vector Table (IVT), and device service mechanisms of the **Intel 8086 Microprocessor**. Key objectives include understanding the 1 KB IVT mapped from `0000:0000H` to `0000:03FFH`, computing 4-byte vector offsets ($4 \times \text{Type}$), installing custom Interrupt Service Routines (ISRs), handling Non-Maskable Interrupts (`NMI` / Type 2), and managing critical sections with `CLI` and `STI`.

---

## 📂 Directory Contents

| Folder | Description | Key Files |
|:---|:---|:---|
| **`Programs/`** | Assembly source programs (`.asm`) | `ProgA_INT40H_Vector_Setup.asm`, `ProgB_NMI_INT02H_Vector.asm`, `ProgC_Interrupt_Masking.asm` |
| **`Evidence/`** | Standardized simulator execution captures | `Exp6_ProgA_INT_40H_Vector.png`, `Exp6_ProgB_NMI_Vector_Setup.png` |
| **`Reports/`** | Formatted submission lab report | `Experiment_6_Interrupt_Handling_and_Device.docx` |

---

## 🔬 Program Index & Key Technical Highlights

### 1. `ProgA_INT40H_Vector_Setup.asm`
- **Objective:** Configure user interrupt `INT 40H` (Vector address: $40\text{H} \times 4 = 0100\text{H}$).
- **Installation:**
  - Extra Segment `ES` points to IVT segment (`0000H`).
  - Base index `BX = 0100H`.
  - Store ISR Offset: `MOV WORD PTR ES:[BX], OFFSET CUSTOM_ISR`.
  - Store ISR Segment: `MOV WORD PTR ES:[BX+2], CS`.
- **Execution:** Main routine triggers `INT 40H`. Processor pushes `FLAGS`, `CS`, `IP`, branches to `CUSTOM_ISR`, performs service routine, and returns via `IRET`.

### 2. `ProgB_NMI_INT02H_Vector.asm`
- **Objective:** Program vector for Type 2 Non-Maskable Interrupt (`NMI`) located at address `0000:0008H`.
- **Significance:** Demonstrates hardware fail-safe handling (power failure / parity check) which bypasses software interrupt masking.

### 3. `ProgC_Interrupt_Masking.asm`
- **Objective:** Critical code segment protection.
- **Mechanism:** `CLI` disables maskable hardware interrupts (`INTR`), critical time-sensitive I/O operations execute, followed by `STI` restoring interrupt recognition.
