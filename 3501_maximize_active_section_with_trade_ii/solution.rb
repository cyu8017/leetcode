# LeetCode 3501 - Maximize Active Section with Trade II
# https://leetcode.com/problems/maximize-active-section-with-trade-ii/

# @param {String} s
# @param {Integer[][]} queries
# @return {Integer[]}
def max_active_sections_after_trade(s, queries)
  ones = 0
  s.each_char { |c| ones += 1 if c == "1" }
  Array.new(queries.length, ones)
end
