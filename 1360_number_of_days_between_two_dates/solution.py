from datetime import date
class Solution:
    def daysBetweenDates(self, date1, date2):
        return abs((date.fromisoformat(date1)-date.fromisoformat(date2)).days)
