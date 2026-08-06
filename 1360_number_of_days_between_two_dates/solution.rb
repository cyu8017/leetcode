# LeetCode 1360 - Number Of Days Between Two Dates
# https://leetcode.com/problems/number-of-days-between-two-dates/

require 'date'
def days_between_dates(date1, date2)
  (Date.parse(date1) - Date.parse(date2)).to_i.abs
end
