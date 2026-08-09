from datetime import datetime
from zoneinfo import ZoneInfo
import os

# =========================================================
# PERSONAL STREAK SETTINGS
# =========================================================

# Aug 9, 2026 starts at Personal Streak 55
START_DATE = datetime(
    2026, 8, 9,
    tzinfo=ZoneInfo("Asia/Kolkata")
).date()

START_STREAK = 55

# Other information shown on the card
TOTAL_CONTRIBUTIONS = "1,187"
TOTAL_DATE = "Feb 19 - Present"

LONGEST_STREAK = "54"
LONGEST_DATE = "Jun 15 - Aug 7"

PERSONAL_STREAK_DATE = "Aug 9 - Present"


# =========================================================
# CALCULATE CURRENT PERSONAL STREAK
# =========================================================

today = datetime.now(
    ZoneInfo("Asia/Kolkata")
).date()

days_passed = (today - START_DATE).days

current_streak = START_STREAK + max(days_passed, 0)


# =========================================================
# CREATE SVG CARD
# =========================================================

svg = f"""
<svg
    width="840"
    height="313"
    viewBox="0 0 840 313"
    xmlns="http://www.w3.org/2000/svg">

    <!-- Background -->
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

    <!-- Divider 1 -->
    <line
        x1="296"
        y1="42"
        x2="296"
        y2="257"
        stroke="#CDD4E0"
        stroke-width="1"
    />

    <!-- Divider 2 -->
    <line
        x1="544"
        y1="42"
        x2="544"
        y2="257"
        stroke="#CDD4E0"
        stroke-width="1"
    />


    <!-- ================= LEFT ================= -->

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


    <!-- ================= CENTER ================= -->

    <!-- Circular streak ring -->
    <circle
        cx="420"
        cy="103"
        r="61"
        fill="none"
        stroke="#6EA8FF"
        stroke-width="8"
    />

    <!-- Small flame -->
    <path
        d="
        M420 24
        C430 36 431 46 423 54
        C436 52 442 62 442 72
        C442 84 432 92 420 92
        C408 92 398 84 398 72
        C398 62 405 55 412 49
        C410 58 416 63 421 60
        C428 55 427 43 420 24 Z
        "
        fill="#6EA8FF"
    />

    <!-- Current streak number -->
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
        {PERSONAL_STREAK_DATE}
    </text>


    <!-- ================= RIGHT ================= -->

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
# SAVE SVG
# =========================================================

os.makedirs("assets", exist_ok=True)

with open(
    "assets/streak-card.svg",
    "w",
    encoding="utf-8"
) as file:
    file.write(svg)

print(
    f"Personal Coding Streak updated: "
    f"{current_streak} days"
)
