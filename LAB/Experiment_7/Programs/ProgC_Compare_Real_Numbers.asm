ORG 100H
JMP START
P     DD 7.25
Q     DD 3.5
BIG   DD ?
SMALL DD ?
START:
FINIT
FLD Q       ; ST(0) = Q
FLD P       ; ST(0) = P, ST(1) = Q
FCOM ST(1)  ; Compare P with Q
FSTSW AX    ; Copy 8087 status word to AX
SAHF        ; Load AH into CPU flags
JA PBIG     ; Jump if P > Q
FSTP SMALL  ; P is smaller
FSTP BIG    ; Q is larger
JMP DONE
PBIG:
FSTP BIG    ; P is larger
FSTP SMALL  ; Q is smaller
DONE:
HLT