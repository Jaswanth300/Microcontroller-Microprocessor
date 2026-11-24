; ==============================================================================
; Experiment 14 - Program A: Block Transfer External RAM to Internal RAM
; Target: 8051 Microcontroller (Keil uVision IDE)
; Author: Naga Jaswanth (Reg. No: 192424300)
; ==============================================================================

ORG 0000H

MOV DPTR, #4000H    ; Source base address in External RAM
MOV R0, #50H        ; Destination base address in Internal RAM
MOV R2, #05H        ; Block size counter (5 bytes)

BACK:
MOVX A, @DPTR       ; Read data byte from External RAM
MOV @R0, A          ; Store byte to Internal RAM
INC DPTR            ; Increment External pointer
INC R0              ; Increment Internal pointer
DJNZ R2, BACK       ; Decrement counter and loop until 0

STOP: SJMP STOP
END
