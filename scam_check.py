"""The scam check: 7 questions for Jev, and the rule that turns its answers into a verdict.

Every script in this folder uses check() from here, so the questions live in one place.
"""
import time

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient()  # reads TYPESAFE_API_KEY, uses jev-latest

# The 7 questions, all answered in one call.
QUESTIONS = {
    # 5 yes/no questions (Noul): each answer is a probability from 0 to 1
    "asks_secret": Noul(instructions="The message asks the reader to share an OTP, PIN, password or card details"),
    "urgency": Noul(instructions="The message pressures the reader to act immediately or threatens a penalty such as a blocked account, cut connection, arrest or legal action"),
    "impersonation": Noul(instructions="The sender claims to be a bank, government office, police, utility, company or delivery service"),
    "action_push": Noul(instructions="The message asks the reader to pay money, click a link, install an app, enter a UPI PIN, or call or message a number"),
    "too_good": Noul(instructions="The message promises a prize, lottery win, refund, reward, loan or easy money"),
    # 1 Choice: which kind of message this is
    "scam_type": Choice(instructions="What kind of message is this", criteria={
        "bill_or_kyc": "Threat about an electricity bill, KYC, SIM card or a blocked account",
        "lottery_or_prize": "Lottery, lucky draw, reward points or prize win",
        "job_or_income": "Work-from-home job, easy daily income or an investment that multiplies money",
        "delivery_or_customs": "Parcel on hold, customs or delivery fee",
        "family_emergency": "Someone posing as family or a friend asking for money urgently",
        "police_or_legal": "Someone claiming to be police, court or a government agency threatening arrest",
        "refund_or_loan": "Tax refund, cashback, payment to receive or an instant loan offer",
        "wrong_transfer": "Someone says they sent you money by mistake and asks you to send it back",
        "not_a_scam": "A normal personal, business or genuine alert message",
    }),
    # 1 Score: how risky, on a scale we define (0 to 3)
    "risk": Score(instructions="How risky this message is for the reader", criteria=[
        "Safe: a normal message",
        "Suspicious: be careful",
        "Likely a scam",
        "Definitely a scam",
    ]),
}

# What each red flag means, for printing
FLAGS = {
    "asks_secret": "OTP / PIN maang raha hai",
    "urgency": "jaldi / dhamki",
    "impersonation": "bank / govt / police banne ki koshish",
    "action_push": "pay / link / call ka push",
    "too_good": "lottery / easy money",
}


def verdict(risk, scam_type):
    """Code decides what to do with Jev's answer. Unsure? Ask the user to verify, never guess."""
    if risk >= 2.0:
        return "SCAM"
    if risk < 0.6 and scam_type == "not_a_scam":
        return "SAFE"
    return "VERIFY"


def check(message):
    """One Jev call -> a small dict with everything a UI needs."""
    start = time.perf_counter()
    response = client.system_one(state=message, questions=QUESTIONS)
    seconds = time.perf_counter() - start
    a = response.answers
    risk = a["risk"].score
    return {
        "verdict": verdict(risk, a["scam_type"].choice),
        "risk": risk,
        "scam_type": a["scam_type"].choice,
        "type_confidence": a["scam_type"].confidence,
        "flags": {name: a[name].noul for name in FLAGS},
        "seconds": seconds,
        "input_tokens": response.usage.input_tokens or 0,
    }
