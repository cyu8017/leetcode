# LeetCode 2485 - Find the Pivot Integer
# https://leetcode.com/problems/find-the-pivot-integer/

# @param {Integer} n
# @return {Integer}
def pivot_integer(n)
  total = n * (n + 1) / 2
  s = 0
  (1..n).each do |x|
    s += x
    return x if s == total - s + x
  end
  -1
end
