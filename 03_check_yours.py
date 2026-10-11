"""Paste any message and Jev checks it. Use this for the messages viewers send in the comments.

Run:   python 03_check_yours.py      (press Enter on an empty line to quit)
Needs: TYPESAFE_API_KEY
"""
from scam_check import FLAGS, check

ADVICE = {
    "SCAM": "Reply mat karo, link mat kholo, kuch share mat karo. Block karo.",
    "VERIFY": "Pakka nahi. Official app ya number se khud check karo, message wale number pe nahi.",
    "SAFE": "Normal message lagta hai.",
}

check("warm up")  # open the connection first, so your first message isn't slower than the rest

while True:
    message = input("\nMessage paste karo (Enter = quit): ").strip()
    if not message:
        break
    r = check(message)
    print(f"\n  {r['verdict']}   risk {r['risk']:.2f} / 3   ({r['seconds']:.2f} s)")
    print(f"  Type: {r['scam_type']} ({r['type_confidence']:.0%} sure)")
    raised = [f"{FLAGS[name]} ({value:.2f})" for name, value in r["flags"].items() if value >= 0.5]
    print("  Red flags: " + (", ".join(raised) if raised else "none"))
    print("  " + ADVICE[r["verdict"]])
