import calendar
import datetime

year = 2020
days = ["月", "火", "水", "木", "金", "土", "日"]

for i in reversed(range(12)):
    month = i+1
    firstday, lastday = calendar.monthrange(year, month)
    print("↓　" + str(year) + "年" + str(month) + "月")
    for d in reversed(range(lastday)):
        print(str(year) + "/" + str(month).zfill(2) + "/" +
              str(d+1).zfill(2) + " (" + days[(d + firstday) % 7] + ")")
    print("↑　" + str(year) + "年" + str(month) + "月")
