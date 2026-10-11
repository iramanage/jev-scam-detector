# Scam detector with Jev: code (Part 2)

One Jev call per message: 7 questions answered at once, then a few lines of plain code decide SCAM, VERIFY or SAFE.

| File | What it does |
|---|---|
| `scam_check.py` | The 7 questions (5 Noul, 1 Choice, 1 Score) and the verdict rule. Every script uses `check()` from here. |
| `01_check_one.py` | One message, one call, the verdict and the red flags. |
| `02_check_twenty.py` | The live test: 20 messages (14 scams, 6 genuine) with verdict, risk, top red flag, time, accuracy and cost. |
| `03_check_yours.py` | Paste any message and check it. Use it for viewers' messages from the comments. |
| `messages.py` | The 20 sample messages. All made up; numbers masked, links broken with `[.]`. |

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

The key goes in a Windows user variable, never in the code:

```powershell
setx TYPESAFE_API_KEY "your-typesafe-key"
```

Close VS Code fully and reopen it after `setx`, so its terminals see the key.

## Run

```bash
python 01_check_one.py
python 02_check_twenty.py
python 03_check_yours.py
```

**Cost:** about 750 input tokens per message at $0.042 per million, so all 20 messages cost well under a tenth of a cent. Output is free.

## The verdict rule

- **SCAM:** risk score 2 or more (out of 3)
- **SAFE:** risk under 0.6 and Jev says it's a normal message
- **VERIFY:** anything in between. Jev isn't sure, so the app tells the user to check through the official app or number. It never guesses.
