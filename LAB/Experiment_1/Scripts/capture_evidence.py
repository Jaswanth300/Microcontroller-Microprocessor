"""
Experiment 1 - Genuine Simulator Evidence Capture Utility
Finds the active Intel 8085 Simulator window, brings it to foreground,
captures the exact window bounds, and saves it directly to Evidence/ directory.
Never creates mockups or fabricates screenshots.
"""

import sys
import os
import time
import argparse
import ctypes
from ctypes import wintypes
from PIL import ImageGrab, Image

user32 = ctypes.windll.user32

PROGRAM_MAP = {
    "A1": "A1_8bit_Addition.png",
    "A2": "A2_8bit_Subtraction.png",
    "B1": "B1_16bit_Addition.png",
    "B2": "B2_16bit_Subtraction.png",
    "C1": "C1_8bit_Multiplication.png",
    "C2": "C2_8bit_Division.png",
    "D1": "D1_16bit_Multiplication.png",
    "D2": "D2_16bit_Division.png"
}

def find_simulator_window():
    candidate_hwnds = []
    def enum_cb(hwnd, lParam):
        if user32.IsWindowVisible(hwnd):
            length = user32.GetWindowTextLengthW(hwnd)
            if length > 0:
                buff = ctypes.create_unicode_buffer(length + 1)
                user32.GetWindowTextW(hwnd, buff, length + 1)
                title = buff.value
                if "Microprocessor 8085" in title or "Code Editor" in title or "MP8085" in title:
                    candidate_hwnds.append((hwnd, title))
        return True

    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
    user32.EnumWindows(EnumWindowsProc(enum_cb), 0)
    return candidate_hwnds

def capture_window(hwnd, output_path):
    # Bring window to foreground
    user32.ShowWindow(hwnd, 9) # SW_RESTORE
    user32.SetForegroundWindow(hwnd)
    time.sleep(0.5)

    rect = wintypes.RECT()
    # Try DwmGetWindowAttribute for accurate borderless rect if available
    try:
        dwmapi = ctypes.windll.dwmapi
        DWMWA_EXTENDED_FRAME_BOUNDS = 9
        dwmapi.DwmGetWindowAttribute(hwnd, DWMWA_EXTENDED_FRAME_BOUNDS, ctypes.byref(rect), ctypes.sizeof(rect))
    except Exception:
        user32.GetWindowRect(hwnd, ctypes.byref(rect))

    bbox = (rect.left, rect.top, rect.right, rect.bottom)
    if bbox[2] <= bbox[0] or bbox[3] <= bbox[1]:
        user32.GetWindowRect(hwnd, ctypes.byref(rect))
        bbox = (rect.left, rect.top, rect.right, rect.bottom)

    # Capture bbox
    img = ImageGrab.grab(bbox=bbox)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")

    # Verify saved image
    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        verified_img = Image.open(output_path)
        print(f"[SUCCESS] Captured simulator window: {output_path}")
        print(f"  Dimensions: {verified_img.size}, File size: {os.path.getsize(output_path)} bytes")
        return True
    else:
        print(f"[ERROR] Failed to save valid image to {output_path}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Capture genuine 8085 simulator window evidence.")
    parser.add_argument("--program", "-p", choices=list(PROGRAM_MAP.keys()), required=True,
                        help="Program code to capture (A1, A2, B1, B2, C1, C2, D1, D2)")
    parser.add_argument("--delay", "-d", type=int, default=0,
                        help="Seconds to wait before capturing (allows user to activate window manually)")

    args = parser.parse_args()
    filename = PROGRAM_MAP[args.program]
    target_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Evidence", filename))

    if args.delay > 0:
        print(f"Waiting {args.delay} seconds for user to switch to simulator window...")
        for i in range(args.delay, 0, -1):
            print(f"  {i}...", flush=True)
            time.sleep(1)

    hwnds = find_simulator_window()
    if not hwnds:
        print("[ERROR] No running Intel 8085 Simulator window found!")
        print("Please ensure MP8085.exe is running with your program assembled and executed.")
        sys.exit(1)

    target_hwnd, title = hwnds[0]
    print(f"Found Simulator window: HWND={target_hwnd}, Title='{title}'")
    success = capture_window(target_hwnd, target_path)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
