#!/usr/bin/env python3

from datetime import datetime, timedelta
import calendar


def gen_progress_bar(progress):
    capacity = 30
    passed_progress_bar_index = int(progress * capacity)
    return '█' * passed_progress_bar_index + '▁' * (capacity - passed_progress_bar_index)


now = datetime.now()
this_year = now.year
this_month = now.month
this_day = now.day
this_date = now.weekday()


# Year Progress
start_time_of_this_year = datetime(this_year, 1, 1, 0, 0, 0).timestamp()
end_time_of_this_year = datetime(this_year, 12, 31, 23, 59, 59).timestamp()
progress_of_this_year = (datetime.now().timestamp() - start_time_of_this_year) / (end_time_of_this_year - start_time_of_this_year)
progress_bar_of_this_year = gen_progress_bar(progress_of_this_year)

# Month Progress
last_day_of_this_month = calendar.monthrange(this_year, this_month)[1]
start_time_of_this_month = datetime(this_year, this_month, 1, 0, 0, 0).timestamp()
end_time_of_this_month = datetime(this_year, this_month, last_day_of_this_month, 23, 59, 59).timestamp()
progress_of_this_month = (datetime.now().timestamp() - start_time_of_this_month) / (end_time_of_this_month - start_time_of_this_month)
progress_bar_of_this_month = gen_progress_bar(progress_of_this_month)

# Week Progress
start_time_of_this_week = (datetime(this_year, this_month, this_day, 0, 0, 0) - timedelta(days=this_date)).timestamp()
end_time_of_this_week = (datetime(this_year, this_month, this_day, 23, 59, 59) + timedelta(days=6 - this_date)).timestamp()
progress_of_this_week = (datetime.now().timestamp() - start_time_of_this_week) / (end_time_of_this_week - start_time_of_this_week)
progress_bar_of_this_week = gen_progress_bar(progress_of_this_week)

# content
readme = f"\
- Year     progress {{ {progress_bar_of_this_year}  }} {round(progress_of_this_year * 100, 2)} %\n\
- Month progress {{ {progress_bar_of_this_month}  }} {round(progress_of_this_month * 100, 2)} %\n\
- Week   progress {{ {progress_bar_of_this_week}  }} {round(progress_of_this_week * 100, 2)} %\n\
\n\
---\n\
\n\
⏰ Updated at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S %p')} UTC\n\
"

# print(readme)

with open('./README.md', 'r', encoding="utf-8") as file:
    content = file.read()
    start_comment = "<!-- Start of Time Progress Bar -->"
    end_comment = "<!-- End of Time Progress Bar -->"
    start_index = content.find(start_comment) + len(start_comment) + 1
    end_index = content.find(end_comment)
    content = content[:start_index] + readme + content[end_index:]

with open('./README.md', 'w', encoding="utf-8") as file:
    file.write(content)
