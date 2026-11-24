; ==============================================================================
; Experiment 14 - Program C: Register Banks, Stack Operations & MOVC Lookup
; Target: 8051 Microcontroller (Keil uVision IDE)
; Author: Naga Jaswanth (Reg. No: 192424300)
; ==============================================================================

ORG 0000H

MOV SP, #2FH        ; Initialize stack pointer above bit-addressable RAM

; Register Bank Switching: Select Bank 1 (RS0=1, RS1=0 -> PSW.3=1)
MOV PSW, #08H
MOV R0, #11H        ; Loads into physical RAM 08H
MOV R1, #22H        ; Loads into physical RAM 09H

; Switch to Bank 0 (PSW = 00H)
MOV PSW, #00H
MOV R0, #33H        ; Loads into physical RAM 00H

; Stack Operations
PUSH 08H            ; Push Bank 1 R0 onto stack
PUSH 09H            ; Push Bank 1 R1 onto stack
POP 08H             ; Pop into physical 08H
POP 09H             ; Pop into physical 09H

; Code Memory Lookup Table using MOVC
MOV DPTR, #TABLE    ; DPTR points to square lookup table in ROM
MOV R2, #04H        ; Count = 4 elements
MOV R1, #60H        ; Destination RAM pointer
MOV R3, #00H        ; Index counter

NEXT:
MOV A, R3
MOVC A, @A+DPTR     ; Read square value from program code memory
MOV @R1, A          ; Store into Internal RAM
INC R1
INC R3
DJNZ R2, NEXT

STOP: SJMP STOP

TABLE:
DB 00H, 01H, 04H, 09H, 10H, 19H, 24H, 31H, 40H, 51H
END
