ORG 100H
JMP START
A    DD 5.5
B    DD 2.5
SUM  DD ?
DIFF DD ?
PROD DD ?
QUOT DD ?
START:
FINIT       ; Reset the 8087
FLD A       ; ST(0) = A (5.5)
FADD B      ; ST(0) = A + B = 8.0
FSTP SUM    ; Store sum and pop
FLD A
FSUB B      ; ST(0) = A - B = 3.0
FSTP DIFF
FLD A
FMUL B      ; ST(0) = A * B = 13.75
FSTP PROD
FLD A
FDIV B      ; ST(0) = A / B = 2.2
FSTP QUOT
HLT