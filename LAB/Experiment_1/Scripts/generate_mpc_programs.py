"""
Generates valid .mpc files for A(1), A(2), C(1), C(2)
Matching Intel 8085 Simulator Software Kit 1.0 format.
Includes RTF assembly, starting address, UserData inputs and expected outputs, and HexData.
"""

import os

def build_rtf_assembly(lines):
    rtf_lines = [
        r"{\rtf1\ansi\ansicpg1252\deff0\deflang1033{\fonttbl{\f0\fnil\fcharset0 Courier New;}}",
        r"{\colortbl ;\red0\green0\blue0;}",
        r"\viewkind4\uc1\pard\li195\cf1\f0\fs20 "
    ]
    for line in lines:
        rtf_lines.append(rf"\par {line}")
    rtf_lines.append(r"\par \cf0 ")
    rtf_lines.append(r"\par }")
    return "\n".join(rtf_lines)

def build_mpc_file(start_addr, asm_lines, user_data_dict, hex_data_list):
    content = []
    content.append(f"{start_addr:04X}")
    content.append(build_rtf_assembly(asm_lines))
    content.append("<End Codes>")
    
    # UserData
    content.append("20")
    for i, (addr, val) in enumerate(user_data_dict.items(), 1):
        content.append(f"{i}| {addr:04X}| {val:02X}")
    content.append("<End UserData>")

    # HexData
    content.append(str(len(hex_data_list) * 3))
    for i, (addr, byte_val) in enumerate(hex_data_list, 1):
        content.append(f"{i}| {addr:04X}| {byte_val:02X}")
    content.append("<End HexData>")
    content.append("")
    content.append("<End Comment>")
    content.append("")

    return "\n".join(content)

def main():
    target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Programs"))
    os.makedirs(target_dir, exist_ok=True)

    # 1. A(1) 8-bit Addition
    a1_asm = [
        "LXI SP 5000h",
        "LDA 4500h",
        "MOV B A",
        "LDA 4501h",
        "ADD B",
        "STA 4502h",
        "PUSH PSW",
        "MVI A 00h",
        "ACI 00h",
        "STA 4503h",
        "POP B",
        "MOV A C",
        "STA 4504h",
        "HLT"
    ]
    a1_ud = {0x4500: 0x9C, 0x4501: 0x7A, 0x4502: 0x16, 0x4503: 0x01, 0x4504: 0x11}
    a1_hex = [
        (0x4100, 0x31), (0x4101, 0x00), (0x4102, 0x50), # LXI SP 5000h
        (0x4103, 0x3A), (0x4104, 0x00), (0x4105, 0x45), # LDA 4500h
        (0x4106, 0x47),                                  # MOV B A
        (0x4107, 0x3A), (0x4108, 0x01), (0x4109, 0x45), # LDA 4501h
        (0x410A, 0x80),                                  # ADD B
        (0x410B, 0x32), (0x410C, 0x02), (0x410D, 0x45), # STA 4502h
        (0x410E, 0xF5),                                  # PUSH PSW
        (0x410F, 0x3E), (0x4110, 0x00),                  # MVI A 00h
        (0x4111, 0xCE), (0x4112, 0x00),                  # ACI 00h
        (0x4113, 0x32), (0x4114, 0x03), (0x4115, 0x45), # STA 4503h
        (0x4116, 0xC1),                                  # POP B
        (0x4117, 0x79),                                  # MOV A C
        (0x4118, 0x32), (0x4119, 0x04), (0x411A, 0x45), # STA 4504h
        (0x411B, 0x76)                                   # HLT
    ]
    p_a1 = os.path.join(target_dir, "A(1) — 8-bit Addition.mpc")
    with open(p_a1, "w", encoding="utf-8") as f:
        f.write(build_mpc_file(0x4100, a1_asm, a1_ud, a1_hex))
    print(f"Generated: {p_a1}")

    # 2. A(2) 8-bit Subtraction
    a2_asm = [
        "LXI SP 5000h",
        "LDA 4501h",
        "MOV B A",
        "LDA 4500h",
        "SUB B",
        "STA 4505h",
        "PUSH PSW",
        "MVI A 00h",
        "ACI 00h",
        "STA 4506h",
        "POP B",
        "MOV A C",
        "STA 4507h",
        "HLT"
    ]
    a2_ud = {0x4500: 0x9C, 0x4501: 0x7A, 0x4505: 0x22, 0x4506: 0x00, 0x4507: 0x14}
    a2_hex = [
        (0x4100, 0x31), (0x4101, 0x00), (0x4102, 0x50), # LXI SP 5000h
        (0x4103, 0x3A), (0x4104, 0x01), (0x4105, 0x45), # LDA 4501h
        (0x4106, 0x47),                                  # MOV B A
        (0x4107, 0x3A), (0x4108, 0x00), (0x4109, 0x45), # LDA 4500h
        (0x410A, 0x90),                                  # SUB B
        (0x410B, 0x32), (0x410C, 0x05), (0x410D, 0x45), # STA 4505h
        (0x410E, 0xF5),                                  # PUSH PSW
        (0x410F, 0x3E), (0x4110, 0x00),                  # MVI A 00h
        (0x4111, 0xCE), (0x4112, 0x00),                  # ACI 00h
        (0x4113, 0x32), (0x4114, 0x06), (0x4115, 0x45), # STA 4506h
        (0x4116, 0xC1),                                  # POP B
        (0x4117, 0x79),                                  # MOV A C
        (0x4118, 0x32), (0x4119, 0x07), (0x411A, 0x45), # STA 4507h
        (0x411B, 0x76)                                   # HLT
    ]
    p_a2 = os.path.join(target_dir, "A(2) — 8-bit Subtraction.mpc")
    with open(p_a2, "w", encoding="utf-8") as f:
        f.write(build_mpc_file(0x4100, a2_asm, a2_ud, a2_hex))
    print(f"Generated: {p_a2}")

    # 3. C(1) 8-bit Multiplication
    c1_asm = [
        "LDA 4520h",
        "MOV E A",
        "MVI D 00h",
        "LDA 4521h",
        "MOV C A",
        "LXI H 0000h",
        "MOV A C",
        "ORA A",
        "JZ DONE",
        "LOOP: DAD D",
        "DCR C",
        "JNZ LOOP",
        "DONE: SHLD 4522h",
        "HLT"
    ]
    c1_ud = {0x4520: 0x12, 0x4521: 0x05, 0x4522: 0x5A, 0x4523: 0x00}
    c1_hex = [
        (0x4300, 0x3A), (0x4301, 0x20), (0x4302, 0x45), # LDA 4520h
        (0x4303, 0x5F),                                  # MOV E A
        (0x4304, 0x16), (0x4305, 0x00),                  # MVI D 00h
        (0x4306, 0x3A), (0x4307, 0x21), (0x4308, 0x45), # LDA 4521h
        (0x4309, 0x4F),                                  # MOV C A
        (0x430A, 0x21), (0x430B, 0x00), (0x430C, 0x00), # LXI H 0000h
        (0x430D, 0x79),                                  # MOV A C
        (0x430E, 0xB7),                                  # ORA A
        (0x430F, 0xCA), (0x4310, 0x17), (0x4311, 0x43), # JZ DONE (4317h)
        (0x4312, 0x19),                                  # LOOP: DAD D
        (0x4313, 0x0D),                                  # DCR C
        (0x4314, 0xC2), (0x4315, 0x12), (0x4316, 0x43), # JNZ LOOP (4312h)
        (0x4317, 0x22), (0x4318, 0x22), (0x4319, 0x45), # DONE: SHLD 4522h
        (0x431A, 0x76)                                   # HLT
    ]
    p_c1 = os.path.join(target_dir, "C(1) — 8-bit Multiplication.mpc")
    with open(p_c1, "w", encoding="utf-8") as f:
        f.write(build_mpc_file(0x4300, c1_asm, c1_ud, c1_hex))
    print(f"Generated: {p_c1}")

    # 4. C(2) 8-bit Division
    c2_asm = [
        "LDA 4524h",
        "MOV B A",
        "LDA 4525h",
        "MOV C A",
        "MVI D 00h",
        "MOV A C",
        "ORA A",
        "JZ ZERO",
        "LOOP: MOV A B",
        "CMP C",
        "JC DONE",
        "SUB C",
        "MOV B A",
        "INR D",
        "JMP LOOP",
        "DONE: MOV A D",
        "STA 4526h",
        "MOV A B",
        "STA 4527h",
        "HLT",
        "ZERO: MVI A FFh",
        "STA 4526h",
        "HLT"
    ]
    c2_ud = {0x4524: 0x64, 0x4525: 0x05, 0x4526: 0x14, 0x4527: 0x00}
    c2_hex = [
        (0x4300, 0x3A), (0x4301, 0x24), (0x4302, 0x45), # LDA 4524h
        (0x4303, 0x47),                                  # MOV B A
        (0x4304, 0x3A), (0x4305, 0x25), (0x4306, 0x45), # LDA 4525h
        (0x4307, 0x4F),                                  # MOV C A
        (0x4308, 0x16), (0x4309, 0x00),                  # MVI D 00h
        (0x430A, 0x79),                                  # MOV A C
        (0x430B, 0xB7),                                  # ORA A
        (0x430C, 0xCA), (0x430D, 0x23), (0x430E, 0x43), # JZ ZERO (4323h)
        (0x430F, 0x78),                                  # LOOP: MOV A B
        (0x4310, 0xB9),                                  # CMP C
        (0x4311, 0xDA), (0x4312, 0x1A), (0x4313, 0x43), # JC DONE (431Ah)
        (0x4314, 0x91),                                  # SUB C
        (0x4315, 0x47),                                  # MOV B A
        (0x4316, 0x14),                                  # INR D
        (0x4317, 0xC3), (0x4318, 0x0F), (0x4319, 0x43), # JMP LOOP (430Fh)
        (0x431A, 0x7A),                                  # DONE: MOV A D
        (0x431B, 0x32), (0x431C, 0x26), (0x431D, 0x45), # STA 4526h
        (0x431E, 0x78),                                  # MOV A B
        (0x431F, 0x32), (0x4320, 0x27), (0x4321, 0x45), # STA 4527h
        (0x4322, 0x76),                                  # HLT
        (0x4323, 0x3E), (0x4324, 0xFF),                  # ZERO: MVI A FFh
        (0x4325, 0x32), (0x4326, 0x26), (0x4327, 0x45), # STA 4526h
        (0x4328, 0x76)                                   # HLT
    ]
    p_c2 = os.path.join(target_dir, "C(2) — 8-bit Division.mpc")
    with open(p_c2, "w", encoding="utf-8") as f:
        f.write(build_mpc_file(0x4300, c2_asm, c2_ud, c2_hex))
    print(f"Generated: {p_c2}")

if __name__ == "__main__":
    main()
