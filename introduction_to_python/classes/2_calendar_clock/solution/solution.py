class Clock:

    def __init__(self,hrs,mins,secs):
        self.hrs = hrs
        self.mins = mins
        self.secs = secs
    def __str__(self):
        return f"{self.hrs}:{self.mins}:{self.secs}"

class Calendar:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def __str__(self):
        return f"{self.day}:{self.month}:{self.year}"

class CalendarClock(Clock,Calendar):

    def __init__(self, day, month, year, hrs, mins, secs):
        Clock.__init__(hrs, mins, secs)
        Calendar.__init__(day, month, year)
    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}, {self.hrs}:{self.mins}:{self.secs}"
















