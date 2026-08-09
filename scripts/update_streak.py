from datetime import datetime
from zoneinfo import ZoneInfo
import os


# =========================================================
# PERSONAL CODING STREAK SETTINGS
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
# CALCULATE CURRENT STREAK
# =========================================================

today = datetime.now(
    ZoneInfo("Asia/Kolkata")
).date()

days_passed = (today - START_DATE).days

current_streak = START_STREAK + max(days_passed, 0)

# Example: Aug 9
current_date_text = f"{today.strftime('%b')} {today.day}"

personal_date = f"{STREAK_START_DATE} - {current_date_text}"


# =========================================================
# CREATE SVG CARD
# =========================================================

svg = f"""<svg
    width="840"
    height="313"
    viewBox="0 0 840 313"
    xmlns="http://www.w3.org/2000/svg">

    <!-- =============================== -->
    <!-- BACKGROUND -->
    <!-- =============================== -->

    <rect
        x="2"
        y="2"
        width="836"
        height="309"
        rx="10"
        fill="#171923"
        stroke="#CDD4E0"
        stroke-width="2"
    />


    <!-- =============================== -->
    <!-- DIVIDERS -->
    <!-- =============================== -->

    <line
        x1="296"
        y1="42"
        x2="296"
        y2="257"
        stroke="#CDD4E0"
        stroke-width="1"
    />

    <line
        x1="544"
        y1="42"
        x2="544"
        y2="257"
        stroke="#CDD4E0"
        stroke-width="1"
    />


    <!-- ================================================= -->
    <!-- LEFT SIDE : TOTAL CONTRIBUTIONS -->
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

    <!-- Streak circle -->
    <circle
        cx="420"
        cy="110"
        r="57"
        fill="none"
        stroke="#6EA8FF"
        stroke-width="8"
    />


    <!-- Clean flame -->
    <path
        d="
        M420 27
        C425 34 430 40 429 47
        C428 52 425 55 421 57

        C422 52 420 48 417 45

        C412 50 409 55 410 61
        C411 68 415 73 421 73

        C428 73 433 68 433 61

        C433 54 429 49 425 44

        C425 49 423 52 420 54

        C422 47 422 37 420 27
        Z"
        fill="#6EA8FF"
    />


    <!-- Personal streak number -->
    <text
        x="420"
        y="127"
        text-anchor="middle"
        font-family="Arial, Helvetica, sans-serif"
        font-size="43"
        font-weight="700"
        fill="#BB86FC">
        {current_streak}
    </text>


    <!-- Personal streak heading -->
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


    <!-- Personal streak dates -->
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
    <!-- RIGHT SIDE : LONGEST STREAK -->
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
# CREATE ASSETS FOLDER
# =========================================================

os.makedirs(
    "assets",
    exist_ok=True
)


# =========================================================
# SAVE SVG CARD
# =========================================================

with open(
    "assets/streak-card.svg",
    "w",
    encoding="utf-8"
) as file:
    file.write(svg)


# =========================================================
# CONSOLE OUTPUT
# =========================================================

print("====================================")
print(" Personal Coding Streak Updated")
print("====================================")
print(f"Current Streak : {current_streak} Days")
print(f"Date           : {personal_date}")
print("====================================")
