# LeetCode 1185 - Day of the Week
# https://leetcode.com/problems/day-of-the-week/

# @param {Integer} day
# @param {Integer} month
# @param {Integer} year
# @return {String}
def day_of_the_week(day, month, year)
  require "date"
  Date.new(year, month, day).strftime("%A")
end
