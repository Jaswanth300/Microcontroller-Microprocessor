; ==============================================================================
; Experiment 14 - Program B: 4-Byte Multi-Byte Addition into External RAM
; Target: 8051 Microcontroller (Keil uVision IDE)
; Author: Naga Jaswanth (Reg. No: 192424300)
; ==============================================================================

ORG 0000H

MOV R0, #40H        ; Operand 1 starting address in Internal RAM
MOV R1, #50H        ; Operand 2 starting address in Internal RAM
MOV DPTR, #4500H    ; Destination starting address in External RAM
MOV R3, #04H        ; Number of bytes = 4
CLR C               ; Clear initial carry

BACK:
MOV A, @R0          ; Read byte from Operand 1
ADDC A, @R1         ; Add byte from Operand 2 with Carry
MOVX @DPTR, A       ; Write sum byte to External RAM
INC R0              ; Increment pointers
INC R1
INC DPTR
DJNZ R3, BACK       ; Loop 4 times

CLR A
ADDC A, #00H        ; Propagate final carry into 5th byte
MOVX @DPTR, A

STOP: SJMP STOP
END
