"""Check one message with Jev: one call, 7 answers, one verdict.

Run:   python 01_check_one.py
Needs: TYPESAFE_API_KEY
"""
from scam_check import FLAGS, check

message = ("Dear Consumer, your electricity power will be disconnected tonight at 9:30 PM because your "
           "previous month bill was not updated. Please immediately contact our electricity officer 98XXX-XX421.")

check("warm up")  # the first call also opens the connection; warm up so the time below is just the check
result = check(message)

print("Verdict:  ", result["verdict"])
print("Risk:     ", f"{result['risk']:.2f} / 3")
print("Type:     ", result["scam_type"], f"({result['type_confidence']:.0%} sure)")
print("Red flags:")
for name, value in result["flags"].items():
    print(f"   {FLAGS[name]:<38} {value:.2f}")
print(f"Time:      {result['seconds']:.2f} s  |  input tokens: {result['input_tokens']}")
