# LeetCode 2777 - Date Range Generator
# https://leetcode.com/problems/date-range-generator/

require "date"

# @param {String} start
# @param {String} last
# @param {Integer} step
# @return {String[]}
def date_range_generator(start, last, step)
  cur = Date.iso8601(start)
  stop = Date.iso8601(last)
  ans = []
  while cur <= stop
    ans << format("%04d-%02d-%02d", cur.year, cur.month, cur.day)
    cur += step
  end
  ans
end
