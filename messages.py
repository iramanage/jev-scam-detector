"""20 sample messages for the live test: 14 scams and 6 genuine ones.

All of them are made up for the demo. Phone numbers are masked and links are broken with [.] so nothing is clickable.
"expected" is what a careful human would say: "scam", or "safe" for genuine messages.
"""

MESSAGES = [
    # ---- scams ----
    ("Bijli cut", "scam", "Dear Consumer, your electricity power will be disconnected tonight at 9:30 PM because your previous month bill was not updated. Please immediately contact our electricity officer 98XXX-XX421."),
    ("KYC block", "scam", "Dear customer, your bank account will be BLOCKED today. Update your KYC now: kyc-verify-online[.]in/upd and share the OTP with our executive to complete."),
    ("Lottery", "scam", "Congratulations! Your number won Rs 25,00,000 in the Lucky Draw 2026. To claim, pay processing fee Rs 4,999 and send your bank details on WhatsApp."),
    ("Ghar baithe job", "scam", "Part time job! Earn Rs 5,000-8,000 daily from home. Just like YouTube videos. No experience needed. Contact HR on Telegram @easyjob_hr"),
    ("Parcel customs", "scam", "Your parcel is on hold at customs. Pay Rs 199 clearance fee within 24 hours or it will be returned: parcel-help[.]co/pay"),
    ("'Mummy' naya number", "scam", "Hi Mummy, this is my new number. Phone kharab ho gaya. Urgent Rs 15,000 chahiye, abhi UPI kar do please, baad mein call karta hoon."),
    ("Digital arrest", "scam", "This is Inspector Sharma from Police Cyber Cell. A parcel with illegal items was booked on your Aadhaar. You are under digital arrest. Stay on video call and do not tell anyone, or a warrant will be issued."),
    ("Tax refund", "scam", "Income Tax Dept: Your refund of Rs 15,490 is approved. Verify your bank account details to receive it today: itr-refund-status[.]in"),
    ("Instant loan", "scam", "Pre-approved instant loan of Rs 5,00,000 at 0% interest! No documents needed. Install the app now to get money in 5 minutes: quickloan-apk[.]in"),
    ("OTP galti se", "scam", "Sorry, I sent a 6-digit code to your number by mistake. Please send it back to me quickly, it is very urgent."),
    ("UPI request", "scam", "You have received Rs 5,000 from Rahul. To accept the money, enter your UPI PIN in the request that just came on your UPI app."),
    ("SIM block", "scam", "Your SIM card will be blocked within 24 hours due to eSIM upgrade. Reply 1 or call 98XXX-XX733 to keep your number active."),
    ("Reward points", "scam", "Dear customer, your 5,999 credit card reward points expire today! Redeem now for cash: rewards-redeem-now[.]com"),
    ("Paisa double", "scam", "Join our VIP Telegram group. Our experts double your money in 30 days. Last week members earned 300% profit. Limited seats, join now!"),
    # ---- genuine ----
    ("Dost: cricket", "safe", "Hi Shubham, kal 6 baje cricket match hai, aa rahe ho? Ground pe milte hain."),
    ("Mummy: khana", "safe", "Beta, khana kha liya? Papa puch rahe the tum Sunday ko ghar aa rahe ho ya nahi."),
    ("Bank OTP (asli)", "safe", "482910 is your OTP to log in to net banking. It is valid for 5 minutes. Do not share it with anyone, including bank staff."),
    ("Debit alert (asli)", "safe", "INR 2,000.00 debited from A/c XX4321 on 07-Oct-26 to UPI merchant. Avl bal INR 18,240.50. Not you? Call the number on the back of your card."),
    ("Order delivered", "safe", "Your order #40213 has been delivered. Hope you like it! You can rate your experience in the app."),
    ("Office meeting", "safe", "Reminder: team meeting moved to 3 PM today in conference room B. Please bring the Q3 numbers."),
]
