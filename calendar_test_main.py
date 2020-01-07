import calendar
import datetime

output_path = "D:\\calendar_test\\nikki.txt"
days = ["月", "火", "水", "木", "金", "土", "日"]


class MakeCalendars:
    def __init__(self):
        self.this_year = 2020

    def make_calendar_text(self, this_year: int):
        self.this_year = this_year
        output = ""
        for i in reversed(range(12)):
            month = i+1
            firstday, lastday = calendar.monthrange(this_year, month)
            output += "↓　" + str(this_year) + "年" + str(month) + "月\n"
            for d in reversed(range(lastday)):
                output += str(this_year) + "/" + str(month).zfill(2) + "/" +str(d+1).zfill(2) + " (" + days[(d + firstday) % 7] + ")\n"
                output += "起床。\n"
                output += "就寝。\n"
            output += "↑　" + str(this_year) + "年" + str(month) + "月\n"

        with open(output_path, mode='w') as f:
            f.write(output)

calendar1 = MakeCalendars()
calendar1.make_calendar_text(2020)
