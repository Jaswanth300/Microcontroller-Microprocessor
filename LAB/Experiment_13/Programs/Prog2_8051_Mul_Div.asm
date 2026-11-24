; ==============================================================================
; Experiment 13 - Program 2: 8051 8-Bit Multiplication and Division
; Target: 8051 Microcontroller (Keil uVision IDE)
; Author: Naga Jaswanth (Reg. No: 192424300)
; ==============================================================================

ORG 0000H

; Multiplication: A * B -> B:A (16-bit Product)
MOV A, 36H          ; Load Multiplicand (e.g. C8H / 200D)
MOV B, 37H          ; Load Multiplier (e.g. 0AH / 10D)
MUL AB              ; Product in B (High Byte) and A (Low Byte)
MOV 38H, A          ; Store Product Low Byte (D0H)
MOV 39H, B          ; Store Product High Byte (07H) -> 07D0H (2000D)

; Division: A / B -> Quotient in A, Remainder in B
MOV A, 3AH          ; Load Dividend (e.g. FFH / 255D)
MOV B, 3BH          ; Load Divisor (e.g. 0DH / 13D)
DIV AB              ; Quotient in A, Remainder in B
MOV 3CH, A          ; Store Quotient (13H / 19D)
MOV 3DH, B          ; Store Remainder (08H / 8D)

STOP: SJMP STOP
END
