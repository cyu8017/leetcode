# LeetCode 1215 - Stepping Numbers
# https://leetcode.com/problems/stepping-numbers/

# @param {Integer} low
# @param {Integer} high
# @return {Integer[]}
def count_stepping_numbers(low, high)
  answer = low == 0 ? [0] : []
  q = (1..9).to_a
  until q.empty?
    x = q.shift
    next if x > high
    answer << x if x >= low
    last = x % 10
    q << x * 10 + last - 1 if last > 0
    q << x * 10 + last + 1 if last < 9
  end
  answer.sort
end
