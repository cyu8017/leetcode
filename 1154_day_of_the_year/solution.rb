# LeetCode 1154 - Day of the Year
# https://leetcode.com/problems/day-of-the-year/

# @param {String} date
# @return {Integer}
def day_of_year(date)
  year, month, day = date.split("-").map(&:to_i)
  leap = year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)
  days = [31, leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  days[0...month - 1].sum + day
end
