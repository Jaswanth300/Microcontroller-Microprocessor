ORG 100H
JMP START
R    DD 3.0
X    DD 144.0
AREA DD ?
ROOT DD ?
START:
FINIT
FLDPI       ; ST(0) = pi (3.14159265...)
FMUL R      ; pi * R
FMUL R      ; pi * R * R (Area = 28.2743)
FSTP AREA   ; Store area
FLD X       ; ST(0) = 144.0
FSQRT       ; ST(0) = sqrt(144.0) = 12.0
FSTP ROOT   ; Store square root
HLT