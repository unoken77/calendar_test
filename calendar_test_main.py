import calendar
import datetime

output_path1 = "D:\\calendar_test\\nikki1.txt"
output_path2 = "D:\\calendar_test\\nikki2.txt"
days = ["月", "火", "水", "木", "金", "土", "日"]


class MakeCalendars:
    def __init__(self):
        self.dt_now = datetime.datetime.now()

    def this_year_calendar(self):
        output = ""
        for i in reversed(range(12)):
            month = i+1
            firstday, lastday = calendar.monthrange(self.dt_now.year, month)
            output += "↓　" + str(self.dt_now.year) + "年" + str(month) + "月\n"
            for d in reversed(range(lastday)):
                output += str(self.dt_now.year) + "/" + str(month).zfill(2) + "/" +str(d+1).zfill(2) + " (" + days[(d + firstday) % 7] + ")\n"
                output += "起床。\n就寝。\n\n"
            output += "↑　" + str(self.dt_now.year) + "年" + str(month) + "月\n"

        with open(output_path1, mode='w', encoding='utf-8') as f:
            f.write(output)

    def chosen_year_calendar(self, the_year: int):
        output = ""
        for i in reversed(range(12)):
            month = i+1
            firstday, lastday = calendar.monthrange(the_year, month)
            output += "↓　" + str(the_year) + "年" + str(month) + "月\n"
            for d in reversed(range(lastday)):
                output += str(the_year) + "/" + str(month).zfill(2) + "/" +str(d+1).zfill(2) + " (" + days[(d + firstday) % 7] + ")\n"
                output += "起床。\n就寝。\n\n"
            output += "↑　" + str(the_year) + "年" + str(month) + "月\n"

        with open(output_path2, mode='w', encoding='utf-8') as f:
            f.write(output)