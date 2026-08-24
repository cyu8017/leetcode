# LeetCode 2758 - Next Day
# https://leetcode.com/problems/next-day/

require "date"

# @param {Object} date_value
# @return {String}
def next_day(date_value)
  d = if date_value.is_a?(Date) || date_value.is_a?(Time)
        date_value.to_date
      else
        Date.iso8601(date_value.to_s[0, 10])
      end
  nxt = d + 1
  format("%04d-%02d-%02d", nxt.year, nxt.month, nxt.day)
end
