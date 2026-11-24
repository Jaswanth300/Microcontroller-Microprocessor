; ==============================================================================
; Experiment 11 - Program B: Reception with Echo and Error Detection
; Target: Intel 8086 Microprocessor with 8253 PIT and 8251 USART
; Author: Naga Jaswanth (Reg. No: 192424300)
; ==============================================================================

MOV DX, 0FF06H      ; 8253 Control Word Register
MOV AL, 0B6H        ; Counter 0, Mode 3, 16-bit binary
OUT DX, AL
MOV DX, 0FF04H      ; 8253 Counter 0 Data Register
MOV AL, 27H
OUT DX, AL
MOV AL, 00H
OUT DX, AL

; 8251 USART Initialization
MOV DX, 0FF12H
MOV AL, 00H
OUT DX, AL
OUT DX, AL
OUT DX, AL
MOV AL, 40H         ; Internal Reset
OUT DX, AL
MOV AL, 4EH         ; Mode: 1 stop bit, no parity, 8 data bits, 16X
OUT DX, AL
MOV AL, 37H         ; Command: TxEN, DTR, RxEN, Error Reset, RTS
OUT DX, AL

MOV DI, 1700H       ; Destination buffer for received characters
MOV CX, 0008H       ; Number of characters to receive
MOV BL, 00H         ; Error counter initialized to 00H

NEXTR:
MOV DX, 0FF12H      ; 8251 Status Register
WAITR:
IN AL, DX
TEST AL, 02H        ; Test RxRDY (Bit 1)
JZ WAITR            ; Wait until character is received
TEST AL, 38H        ; Test Parity (Bit 3), Overrun (Bit 4), Framing (Bit 5) Errors
JZ NOERR            ; Jump if error-free
INC BL              ; Increment error count
MOV AL, 37H         ; Reset Error Flags in 8251 Command Register
OUT DX, AL

NOERR:
MOV DX, 0FF10H      ; 8251 Data Register
IN AL, DX           ; Read received character
MOV [DI], AL        ; Store in receive buffer
INC DI
MOV AH, AL          ; Save received character for echo transmission

; Echo received character back to PC terminal
MOV DX, 0FF12H
WAITE:
IN AL, DX
TEST AL, 01H        ; Test TxRDY
JZ WAITE            ; Wait until transmitter is ready
MOV AL, AH
MOV DX, 0FF10H
OUT DX, AL          ; Echo byte
LOOP NEXTR

MOV [1710H], BL     ; Store error count at address 1710H
HLT
