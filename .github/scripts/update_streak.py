from datetime import datetime
from zoneinfo import ZoneInfo
import re

# Aug 9, 2026 = streak day 55
START_DATE = datetime(2026, 8, 9, tzinfo=ZoneInfo("Asia/Kolkata")).date()
START_STREAK = 55

today = datetime.now(ZoneInfo("Asia/Kolkata")).date()

days_passed = (today - START_DATE).days

streak = START_STREAK + max(days_passed, 0)

with open("README.md", "r", encoding="utf-8") as file:
    readme = file.read()

new_section = f"""<!-- PERSONAL_STREAK_START -->
<p align="center">
  <img src="https://img.shields.io/badge/🔥%20Personal%20Coding%20Streak-{streak}%20Days-9B59E6?style=for-the-badge&labelColor=1a1b27" />
</p>
<!-- PERSONAL_STREAK_END -->"""

readme = re.sub(
    r"<!-- PERSONAL_STREAK_START -->.*?<!-- PERSONAL_STREAK_END -->",
    new_section,
    readme,
    flags=re.DOTALL,
)

with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme)

print(f"Personal Coding Streak updated to {streak} days")
