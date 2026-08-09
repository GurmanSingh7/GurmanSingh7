from datetime import datetime
from zoneinfo import ZoneInfo
import os

# =========================================================
# PERSONAL CODING STREAK
# =========================================================

# Aug 9, 2026 = Personal Streak Day 55
START_DATE = datetime(
    2026, 8, 9,
    tzinfo=ZoneInfo("Asia/Kolkata")
).date()

START_STREAK = 55

# Information displayed on the card
TOTAL_CONTRIBUTIONS = "1,187"
TOTAL_DATE = "Feb 19 - Present"

LONGEST_STREAK = "54"
LONGEST_DATE = "Jun 15 - Aug 7"

STREAK_START_DATE = "Aug 9"


# =========================================================
# CALCULATE STREAK
# =========================================================

today = datetime.now(
    ZoneInfo("Asia/Kolkata")
).date()

days_passed = (today - START_DATE).days

current_streak = START_STREAK + max(days_passed, 0)

current_date_text = today.strftime("%b %-d")

personal_date = f"{STREAK_START_DATE} - {current_date_text}"


# =========================================================
# SVG CARD
# =========================================================

svg = f"""<svg width="840" height="313"
viewBox="0 0 840 313"
xmlns="http://www.w3.org/2000/svg">

<rect
    x="2"
    y="2"
    width="836"
    height="309"
    rx="9"
    fill="#171923"
    stroke="#CDD4E0"
    stroke-width="2"
/>

<!-- LEFT DIVIDER -->

<line
    x1="296"
    y1="42"
    x2="296"
    y2="257"
    stroke="#CDD4E0"
    stroke-width="1"
/>

<!-- RIGHT DIVIDER -->

<line
    x1="544"
    y1="42"
    x2="544"
    y2="257"
    stroke="#CDD4E0"
    stroke-width="1"
/>


<!-- ================================================= -->
<!-- LEFT : TOTAL CONTRIBUTIONS -->
<!-- ================================================= -->

<text
    x="171"
    y="122"
    text-anchor="middle"
    font-family="Arial, Helvetica, sans-serif"
    font-size="46"
    font-weight="700"
    fill="#6EA8FF">
    {TOTAL_CONTRIBUTIONS}
</text>

<text
    x="171"
    y="176"
    text-anchor="middle"
    font-family="Arial, Helvetica, sans-serif"
    font-size="21"
    fill="#6EA8FF">
    Total Contributions
</text>

<text
    x="171"
    y="222"
    text-anchor="middle"
    font-family="Arial, Helvetica, sans-serif"
    font-size="17"
    fill="#42D6C8">
    {TOTAL_DATE}
</text>


<!-- ================================================= -->
<!-- CENTER : PERSONAL STREAK -->
<!-- ================================================= -->

<circle
    cx="420"
    cy="103"
    r="61"
    fill="none"
    stroke="#6EA8FF"
    stroke-width="8"
/>

<!-- FLAME -->

<path
    d="
    M420 24
    C430 36 431 46 423 54
    C436 52 442 62 442 72
    C442 84 432 92 420 92
    C408 92 398 84 398 72
    C398 62 405 55 412 49
    C410 58 416 63 421 60
    C428 55 427 43 420 24 Z"
    fill="#6EA8FF"
/>

<!-- STREAK NUMBER -->

<text
    x="420"
    y="119"
    text-anchor="middle"
    font-family="Arial, Helvetica, sans-serif"
    font-size="43"
    font-weight="700"
    fill="#BB86FC">
    {current_streak}
</text>

<text
    x="420"
    y="207"
    text-anchor="middle"
    font-family="Arial, Helvetica, sans-serif"
    font-size="20"
    font-weight="700"
    fill="#C89AF7">
    Personal Streak
</text>

<text
    x="420"
    y="251"
    text-anchor="middle"
    font-family="Arial, Helvetica, sans-serif"
    font-size="17"
    fill="#42D6C8">
    {personal_date}
</text>


<!-- ================================================= -->
<!-- RIGHT : LONGEST STREAK -->
<!-- ================================================= -->

<text
    x="669"
    y="122"
    text-anchor="middle"
    font-family="Arial, Helvetica, sans-serif"
    font-size="46"
    font-weight="700"
    fill="#6EA8FF">
    {LONGEST_STREAK}
</text>

<text
    x="669"
    y="176"
    text-anchor="middle"
    font-family="Arial, Helvetica, sans-serif"
    font-size="21"
    fill="#6EA8FF">
    Longest Streak
</text>

<text
    x="669"
    y="222"
    text-anchor="middle"
    font-family="Arial, Helvetica, sans-serif"
    font-size="17"
    fill="#42D6C8">
    {LONGEST_DATE}
</text>

</svg>
"""


# =========================================================
# CREATE ASSETS FOLDER + SAVE CARD
# =========================================================

os.makedirs("assets", exist_ok=True)

with open(
    "assets/streak-card.svg",
    "w",
    encoding="utf-8"
) as file:
    file.write(svg)

print("====================================")
print("Personal Coding Streak Updated")
print(f"Current Streak : {current_streak} Days")
print(f"Date           : {personal_date}")
print("====================================")
