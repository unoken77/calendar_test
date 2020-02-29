import calendar
import datetime

file_name = ".\\nikki"
days = ["月", "火", "水", "木", "金", "土", "日"]
months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days_english=["Mon.", "Tue.", "Wed.", "Thur.", "Fri.", "Sat.", "Sun."]

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

        with open(file_name+str(self.dt_now.year)+".txt", mode='w', encoding='utf-8') as f:
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

        with open(file_name+str(the_year)+".txt", mode='w', encoding='utf-8') as f:
            f.write(output)

    def this_year_calendar_in_english(self):
        output = ""
        for i in reversed(range(12)):
            month = i+1
            firstday, lastday = calendar.monthrange(self.dt_now.year, month)
            output += "↓  " + months[month-1]+" "+str(self.dt_now.year)+"\n"
            for d in reversed(range(lastday)):
                #output += str(self.dt_now.year) + "/" + str(month).zfill(2) + "/" +str(d+1).zfill(2) + " (" + days[(d + firstday) % 7] + ")\n"
                output += months[month-1]+ " "+str(d+1)+" (" + days_english[(d + firstday) % 7] + ")\n\n"
            output += "↑  " + months[month-1]+" "+str(self.dt_now.year)+"\n"

        with open(file_name+str(self.dt_now.year)+".txt", mode='w', encoding='utf-8') as f:
            f.write(output)