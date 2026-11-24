; ==============================================================================
; Experiment 13 - Program 3: 8051 Logical and Bit-Manipulation Operations
; Target: 8051 Microcontroller (Keil uVision IDE)
; Author: Naga Jaswanth (Reg. No: 192424300)
; ==============================================================================

ORG 0000H

MOV R0, 40H         ; Load input byte from RAM 40H (e.g. A5H = 1010 0101B)

; Bitwise OR with mask
MOV A, R0
ORL A, #0FH         ; A = A5H | 0FH = AFH
MOV 41H, A

; Bitwise AND with mask
MOV A, R0
ANL A, #0F0H        ; A = A5H & F0H = A0H
MOV 42H, A

; Bitwise XOR with mask
MOV A, R0
XRL A, #0FFH        ; A = A5H ^ FFH = 5AH (1's complement)
MOV 43H, A

; Nibble Swapping
MOV A, R0
SWAP A              ; Swap upper and lower nibbles (5AH)
MOV 44H, A

; Rotate Left & Right
MOV A, R0
RL A                ; Rotate accumulator left circular (4BH)
MOV 45H, A
MOV A, R0
RR A                ; Rotate accumulator right circular (D2H)
MOV 46H, A

; Bit Addressable Operations in RAM 20H
MOV 20H, #00H       ; Clear bit-addressable byte 20H
SETB 00H            ; Set bit 20.0
SETB 07H            ; Set bit 20.7
MOV A, R0
MOV C, ACC.0        ; Copy bit 0 of A into Carry
MOV 01H, C          ; Store Carry to bit 20.1
CPL 00H             ; Complement bit 20.0
MOV 47H, 20H        ; Store final bit-addressable byte at 47H

STOP: SJMP STOP
END
