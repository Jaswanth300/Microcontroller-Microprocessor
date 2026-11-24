; ==============================================================================
; Experiment 13 - Program 1: 8051 8-Bit Addition and Subtraction
; Target: 8051 Microcontroller (Keil uVision IDE)
; Author: Naga Jaswanth (Reg. No: 192424300)
; ==============================================================================

ORG 0000H           ; Reset vector

MOV A, 30H          ; Load first operand from RAM 30H (e.g. B5H)
ADD A, 31H          ; Add second operand from RAM 31H (e.g. 6EH)
MOV 32H, A          ; Store 8-bit sum at RAM 32H (23H)
MOV 33H, PSW        ; Store Program Status Word (flags CY, AC, OV, P) at 33H

CLR C               ; Clear borrow flag before subtraction
MOV A, 30H          ; Reload first operand
SUBB A, 31H         ; Subtract second operand with borrow
MOV 34H, A          ; Store difference at RAM 34H (47H)
MOV 35H, PSW        ; Store PSW flags at RAM 35H

STOP: SJMP STOP     ; Terminate execution loop
END
