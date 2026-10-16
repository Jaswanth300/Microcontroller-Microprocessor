"""
Experiment 1 - Result Validation Script
Compares observed memory outputs from .mpc and simulator evidence against authoritative expected values.
Maintains separate expected and observed fields.
Outputs validation status to JSON and Markdown logs.
"""

import os
import re
import json

def parse_user_data_from_mpc(mpc_path):
    if not os.path.exists(mpc_path):
        return None
    with open(mpc_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    user_data = {}
    ud_match = re.search(r"<End Codes>\s*\d+\s*(.*?)\s*<End UserData>", content, re.DOTALL)
    if ud_match:
        for line in ud_match.group(1).strip().split("\n"):
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 3:
                user_data[parts[1].upper()] = parts[2].upper()
    return user_data

def main():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    programs_dir = os.path.join(root, "Experiment_1", "Programs")
    evidence_dir = os.path.join(root, "Experiment_1", "Evidence")
    logs_dir = os.path.join(root, "Experiment_1", "Logs")
    os.makedirs(logs_dir, exist_ok=True)

    test_specs = [
        {
            "id": "A1",
            "name": "8-bit Addition",
            "section": "A(1)",
            "start_address": "4100H",
            "inputs": {"4500": "9C", "4501": "7A"},
            "expected_outputs": {"4502": "16", "4503": "01", "4504": "11"},
            "mpc_file": "A(1) — 8-bit Addition.mpc",
            "evidence_image": "A1_8bit_Addition.png"
        },
        {
            "id": "A2",
            "name": "8-bit Subtraction",
            "section": "A(2)",
            "start_address": "4100H",
            "inputs": {"4500": "9C", "4501": "7A"},
            "expected_outputs": {"4505": "22", "4506": "00", "4507": "14"},
            "mpc_file": "A(2) — 8-bit Subtraction.mpc",
            "evidence_image": "A2_8bit_Subtraction.png"
        },
        {
            "id": "B1",
            "name": "16-bit Addition",
            "section": "B(1)",
            "start_address": "4200H",
            "inputs": {"4510": "34", "4511": "12", "4512": "78", "4513": "56"},
            "expected_outputs": {"4514": "AC", "4515": "68", "4516": "00"},
            "mpc_file": "B(1) — 16-bit Addition.mpc",
            "evidence_image": "B1_16bit_Addition.png"
        },
        {
            "id": "B2",
            "name": "16-bit Subtraction",
            "section": "B(2)",
            "start_address": "4200H",
            "inputs": {"4510": "34", "4511": "12", "4512": "78", "4513": "56"},
            "expected_outputs": {"4518": "BC", "4519": "BB", "451A": "01"},
            "mpc_file": "B(1) — 16-bit Subtraction.mpc",
            "evidence_image": "B2_16bit_Subtraction.png"
        },
        {
            "id": "C1",
            "name": "8-bit Multiplication",
            "section": "C(1)",
            "start_address": "4300H",
            "inputs": {"4520": "12", "4521": "05"},
            "expected_outputs": {"4522": "5A", "4523": "00"},
            "mpc_file": "C(1) — 8-bit Multiplication.mpc",
            "evidence_image": "C1_8bit_Multiplication.png"
        },
        {
            "id": "C2",
            "name": "8-bit Division",
            "section": "C(2)",
            "start_address": "4300H",
            "inputs": {"4524": "64", "4525": "05"},
            "expected_outputs": {"4526": "14", "4527": "00"},
            "mpc_file": "C(2) — 8-bit Division.mpc",
            "evidence_image": "C2_8bit_Division.png"
        },
        {
            "id": "D1",
            "name": "16-bit Multiplication",
            "section": "D(1)",
            "start_address": "4400H",
            "inputs": {"4530": "34", "4531": "12", "4532": "78", "4533": "56"},
            "expected_outputs": {"4534": "60", "4535": "00", "4536": "26", "4537": "06"},
            "mpc_file": "D(1) — 16-bit Multiplication.mpc",
            "evidence_image": "D1_16bit_Multiplication.png"
        },
        {
            "id": "D2",
            "name": "16-bit Division",
            "section": "D(2)",
            "start_address": "442DH",
            "inputs": {"4538": "78", "4539": "56", "453A": "34", "453B": "12"},
            "expected_outputs": {"453C": "04", "453D": "00", "453E": "A8", "453F": "0D"},
            "mpc_file": "D(2) — 16-bit Division.mpc",
            "evidence_image": "D2_16bit_Division.png"
        }
    ]

    results = []
    for test in test_specs:
        item = {
            "id": test["id"],
            "name": test["name"],
            "section": test["section"],
            "start_address": test["start_address"],
            "mpc_file": test["mpc_file"],
            "evidence_image": test["evidence_image"],
            "inputs": test["inputs"],
            "expected_outputs": test["expected_outputs"],
            "observed_inputs": {},
            "observed_outputs": {},
            "has_mpc": False,
            "has_evidence": False,
            "validation_status": "PENDING",
            "notes": ""
        }

        # Check evidence image
        img_path = os.path.join(evidence_dir, test["evidence_image"])
        item["has_evidence"] = os.path.exists(img_path)

        # Check MPC file
        if test["mpc_file"]:
            mpc_p = os.path.join(programs_dir, test["mpc_file"])
            if not os.path.exists(mpc_p):
                # Check root
                mpc_p = os.path.join(root, test["mpc_file"])
            if os.path.exists(mpc_p):
                item["has_mpc"] = True
                ud = parse_user_data_from_mpc(mpc_p)
                for addr in test["inputs"]:
                    if addr in ud:
                        item["observed_inputs"][addr] = ud[addr]
                for addr in test["expected_outputs"]:
                    if addr in ud:
                        item["observed_outputs"][addr] = ud[addr]

                # Validate
                all_matched = True
                missing_any = False
                for addr, exp_val in test["expected_outputs"].items():
                    if addr not in item["observed_outputs"]:
                        missing_any = True
                        all_matched = False
                    elif item["observed_outputs"][addr] != exp_val:
                        all_matched = False

                if missing_any:
                    item["validation_status"] = "PARTIAL"
                    item["notes"] = "Some expected addresses missing in MPC UserData"
                elif all_matched:
                    item["validation_status"] = "PASS"
                    item["notes"] = "Observed values match expected specifications exactly"
                else:
                    item["validation_status"] = "FAIL"
                    item["notes"] = "Mismatch between expected and observed values"
            else:
                item["validation_status"] = "PENDING"
                item["notes"] = "Source .mpc file not found"
        else:
            item["validation_status"] = "PENDING"
            item["notes"] = "Program implementation pending execution in simulator"

        results.append(item)

    # Write JSON log
    out_json = os.path.join(logs_dir, "validation_results.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    # Write Markdown summary
    out_md = os.path.join(logs_dir, "validation_summary.md")
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("# Experiment 1: Execution & Verification Status Log\n\n")
        f.write("| ID | Section | Program Name | Start Addr | MPC Available | Evidence Image | Status | Notes |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
        for r in results:
            mpc_str = f"`{r['mpc_file']}`" if r['has_mpc'] else "*Pending*"
            img_str = f"✅ `{r['evidence_image']}`" if r['has_evidence'] else "⏳ *Pending*"
            badge = f"**{r['validation_status']}**" if r['validation_status'] == "PASS" else f"*{r['validation_status']}*"
            f.write(f"| {r['id']} | {r['section']} | {r['name']} | `{r['start_address']}` | {mpc_str} | {img_str} | {badge} | {r['notes']} |\n")

        f.write("\n\n## Memory Verification Breakdown\n\n")
        for r in results:
            f.write(f"### {r['section']} {r['name']} (`{r['start_address']}`)\n\n")
            f.write(f"- **Validation Status**: `{r['validation_status']}`\n")
            f.write(f"- **Evidence Screenshot**: {'Found' if r['has_evidence'] else 'Pending genuine simulator capture'}\n")
            f.write("- **Memory Comparison Table**:\n\n")
            f.write("  | Address | Role | Expected Value | Observed Value | Match? |\n")
            f.write("  | :--- | :--- | :--- | :--- | :--- |\n")
            for a, v in r["inputs"].items():
                obs = r["observed_inputs"].get(a, "N/A")
                f.write(f"  | `{a}H` | Input | `{v}H` | `{obs}H` | {'MATCH' if obs==v else 'N/A'} |\n")
            for a, v in r["expected_outputs"].items():
                obs = r["observed_outputs"].get(a, "N/A")
                match_str = "MATCH" if obs == v else ("FAIL" if obs != "N/A" else "PENDING")
                f.write(f"  | `{a}H` | Output | `{v}H` | `{obs}H` | **{match_str}** |\n")
            f.write("\n")

    print(f"Validation complete. Results saved to:\n  - {out_json}\n  - {out_md}")

if __name__ == "__main__":
    main()
