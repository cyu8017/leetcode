# LeetCode 3871 - Count Commas in Range II
# https://leetcode.com/problems/count-commas-in-range-ii/

# @param {Integer} n
# @return {Integer}
def count_commas(n)
  ans = 0
  x = 1000
  while x <= n
    ans += n - x + 1
    x *= 1000
  end
  ans
end
