# LeetCode 1118 - Number of Days in a Month
# https://leetcode.com/problems/number-of-days-in-a-month/

# @param {Integer} year
# @param {Integer} month
# @return {Integer}
def number_of_days(year, month)
  days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  return days[month] if month != 2
  leap = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)
  leap ? 29 : 28
end
