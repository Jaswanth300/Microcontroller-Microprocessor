# Experiment 18: Design and Simulation of a Multi-Floor Elevator Controller using PIC18F45K22 Microcontroller

**Student Name:** Naga Jaswanth  
**Register Number:** 192424300  
**Course Code:** ECA1011 — Microprocessors and Microcontrollers (CO5)  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences  
**Lab Date:** 21/11/26  
**Status:** `Completed & Verified ✅`

---

## 📌 Experiment Overview
This laboratory module investigates embedded control engineering using the **Microchip PIC18F45K22 Microcontroller** (Harvard RISC architecture) within **MPLAB X IDE** (XC8 Compiler / MPASM) and **Proteus Simulation Software**. The system implements an automated 4-floor elevator control system featuring elevator call push buttons, a 4-phase stepper motor driven by a ULN2003 driver, a 7-segment floor display, direction indicator LEDs (UP, DOWN), and a DOOR status indicator.

---

## 📂 Directory Contents

| Folder | Description | Key Files |
|:---|:---|:---|
| **`Programs/`** | C & Assembly source programs | `Elevator_Controller_XC8.c`, `Elevator_Controller_MPASM.asm` |
| **`Evidence/`** | Proteus simulation schematic captures | `Exp18_PIC18F45K22_Elevator_Proteus_Simulation.png` |
| **`Reports/`** | Formatted submission lab report | `Experiment_18_Report.docx` |

---

## 🔬 System Specifications & Algorithm

### 1. Hardware Pin Mapping
- **Floor Call Push Buttons:** `RB0` (Floor 0), `RB1` (Floor 1), `RB2` (Floor 2), `RB3` (Floor 3) with weak pull-ups enabled (`WPUB`).
- **ULN2003 Stepper Motor Driver:** `RD0`–`RD3` driving stepper coils ($A, B, C, D$) with 200 steps per floor transition at 10 ms step intervals.
- **Seven-Segment Display:** `RC0`–`RC6` displaying current floor numbers ($0, 1, 2, 3$).
- **Status LEDs:** `RA0` (UP indicator), `RA1` (DOWN indicator), `RA2` (DOOR open indicator, 2-second timeout).

### 2. Elevator Control Algorithm (LOOK Scheduling)
- Implemented as a hierarchical state machine: `IDLE`, `UP`, `DOWN`, `DOOR`.
- Request latching stores incoming passenger calls even while the car is in motion.
- Serves all pending calls in the current direction before reversing, optimizing travel time and motor energy consumption.
