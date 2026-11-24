# Experiment 11: Serial Communication between 8086 Microprocessor and PC using 8251 USART and 8253 Timer

**Student Name:** Naga Jaswanth  
**Register Number:** 192424300  
**Course Code:** ECA1011 — Microprocessors and Microcontrollers  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences  
**Lab Date:** 20/11/26  
**Status:** `Completed & Verified ✅`

---

## 📌 Experiment Overview
This laboratory module investigates asynchronous serial communication interfacing between the **Intel 8086 Microprocessor** and a host PC using the **Intel 8251 Universal Synchronous/Asynchronous Receiver/Transmitter (USART)** and the **Intel 8253 Programmable Interval Timer (PIT)**. The timer generates the baud rate clock square wave (Mode 3), while the 8251 handles serial character serialization, deserialization, status polling (`TxRDY`, `RxRDY`), character echoing, and communication error checking (Parity, Overrun, Framing errors).

---

## 📂 Directory Contents

| Folder | Description | Key Files |
|:---|:---|:---|
| **`Programs/`** | Assembly source programs (`.asm`) | `ProgA_USART_Init_Tx.asm`, `ProgB_USART_Rx_Echo.asm` |
| **`Evidence/`** | Terminal & memory execution captures | `Exp11_ProgA_USART_Tx_Terminal.png`, `Exp11_ProgB_USART_Rx_Echo_Memory.png` |
| **`Reports/`** | Formatted submission lab report | `Experiment_11_Report.docx` |

---

## 🔬 Program Index & Key Technical Highlights

### 1. `ProgA_USART_Init_Tx.asm` (USART Initialisation and String Transmission)
- **8253 Timer Initialization:**
  - Control Word `0B6H` written to `0FF06H` (Counter 0, Mode 3 square-wave generator, 16-bit binary).
  - Count divisor `0027H` (39D) written to `0FF04H` to output baud rate clock.
- **8251 USART Initialization:**
  - Three dummy `00H` bytes written to command register `0FF12H` to synchronize internal state machine.
  - Reset command `40H` issued.
  - Mode Word `4EH`: 1 stop bit, no parity, 8-bit character, 16X baud rate multiplier.
  - Command Word `37H`: `TxEN=1`, `DTR=1`, `RxEN=1`, `Error Reset=1`, `RTS=1`.
- **String Transmission:**
  - Polls `TxRDY` status bit (`Bit 0` of `0FF12H`).
  - Reads string characters from memory `1650H` and writes to data register `0FF10H`.

### 2. `ProgB_USART_Rx_Echo.asm` (String Reception, Character Echo & Error Detection)
- **Reception:**
  - Polls `RxRDY` status bit (`Bit 1` of `0FF12H`).
  - Reads received byte from `0FF10H` and stores in memory buffer starting at `1700H`.
- **Error Detection:**
  - Inspects `PE` (Parity Error, Bit 3), `OE` (Overrun Error, Bit 4), `FE` (Framing Error, Bit 5) via `TEST AL, 38H`.
  - Increments error counter and resets error flags via `37H` to command port.
  - Final error count stored at memory address `1710H` (`00H` verified).
- **Echo Transmission:**
  - Transmits received byte back to PC serial terminal upon `TxRDY` readiness.
