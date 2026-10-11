"""The live test: run all 20 messages through Jev and see how many it gets right.

Run:   python 02_check_twenty.py
Needs: TYPESAFE_API_KEY. Cost: about 20 x 650 input tokens, roughly $0.0006 in total.
"""
from messages import MESSAGES
from scam_check import FLAGS, check

JEV_PRICE = 0.042  # USD per 1M input tokens; output is free
COLOUR = {"SCAM": "\033[91m", "VERIFY": "\033[93m", "SAFE": "\033[92m"}
RESET = "\033[0m"

check("warm up")  # open the connection first, so message 1 isn't slower than the rest

print(f"{'#':<4}{'message':<22}{'verdict':<10}{'risk':<8}{'top red flag':<46}{'time'}")
print("-" * 98)
right = total_time = total_tokens = 0
for i, (name, expected, text) in enumerate(MESSAGES, 1):
    r = check(text)
    top = max(r["flags"], key=r["flags"].get)
    flag = f"{FLAGS[top]} ({r['flags'][top]:.2f})" if r["flags"][top] >= 0.5 else "-"
    # SCAM is right for scams. For genuine messages, SAFE is right and VERIFY is acceptable: it never calls them scams.
    ok = r["verdict"] == "SCAM" if expected == "scam" else r["verdict"] in ("SAFE", "VERIFY")
    right += ok
    total_time += r["seconds"]
    total_tokens += r["input_tokens"]
    v = f"{COLOUR[r['verdict']]}{r['verdict']:<10}{RESET}"
    print(f"{i:<4}{name:<22}{v}{r['risk']:<8.2f}{flag:<46}{r['seconds']:.2f} s  {'✓' if ok else '✗'}")

print("-" * 98)
print(f"Correct:            {right} / {len(MESSAGES)}")
print(f"Average time:       {total_time / len(MESSAGES):.2f} s per message")
print(f"Cost for all 20:    ${total_tokens * JEV_PRICE / 1_000_000:.6f}  ({total_tokens:,} input tokens)")
print(f"At 1 crore / day:   ${total_tokens / len(MESSAGES) * 10_000_000 * JEV_PRICE / 1_000_000:,.0f} per day")
