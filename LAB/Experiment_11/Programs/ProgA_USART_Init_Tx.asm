; ==============================================================================
; Experiment 11 - Program A: USART Initialisation and String Transmission
; Target: Intel 8086 Microprocessor with 8253 PIT and 8251 USART
; Author: Naga Jaswanth (Reg. No: 192424300)
; ==============================================================================

MOV DX, 0FF06H      ; 8253 Control Word Register
MOV AL, 0B6H        ; Counter 0, Mode 3 (Square Wave Generator), 16-bit binary
OUT DX, AL
MOV DX, 0FF04H      ; 8253 Counter 0 Data Register
MOV AL, 27H         ; Divisor Low Byte (Count = 27H / 39D for baud rate clock)
OUT DX, AL
MOV AL, 00H         ; Divisor High Byte
OUT DX, AL

; 8251 USART Initialization Sequence (3 dummy zeros + Reset)
MOV DX, 0FF12H      ; 8251 Control / Command Register
MOV AL, 00H
OUT DX, AL
OUT DX, AL
OUT DX, AL
MOV AL, 40H         ; Internal Reset Command
OUT DX, AL
MOV AL, 4EH         ; Mode Instruction: 1 Stop Bit, No Parity, 8-Bit Character, 16X Baud Rate
OUT DX, AL
MOV AL, 37H         ; Command Instruction: TxEN=1, DTR=1, RxEN=1, Error Reset=1, RTS=1
OUT DX, AL

; Transmit String from Memory 1650H
MOV SI, 1650H       ; Source Buffer Pointer
MOV CX, 0008H       ; String Length (8 Bytes: "MPMC8086")

NEXTC:
MOV DX, 0FF12H      ; 8251 Status Register
WAITT:
IN AL, DX
TEST AL, 01H        ; Test TxRDY (Bit 0)
JZ WAITT            ; Loop until transmitter buffer is empty
MOV AL, [SI]        ; Read character from memory
MOV DX, 0FF10H      ; 8251 Data Register
OUT DX, AL          ; Transmit byte to PC serial port
INC SI              ; Next character
LOOP NEXTC

HLT                 ; Halt Execution
