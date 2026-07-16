# LeetCode 1507

class Solution:
    def reformatDate(self, date):
        months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        day, month, year = date.split()
        return f"{year}-{months.index(month)+1:02d}-{int(day[:-2]):02d}"
