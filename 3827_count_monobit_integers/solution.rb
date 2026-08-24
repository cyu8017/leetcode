# LeetCode 3827 - Count Monobit Integers
# https://leetcode.com/problems/count-monobit-integers/

# @param {Integer} n
# @return {Integer}
def count_monobit(n)
  ans = 1
  i = 1
  x = 1
  while x <= n
    ans += 1
    x += 1 << i
    i += 1
  end
  ans
end
