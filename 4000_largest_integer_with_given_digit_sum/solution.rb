# LeetCode 4000 - Largest Integer With Given Digit Sum
# https://leetcode.com/problems/largest-integer-with-given-digit-sum/

# @param {Integer} n
# @param {Integer} s
# @return {Integer}
def largest_integer(n, s)
  return -1 if n * 9 < s
  ans = 0
  n.times do
    x = s < 9 ? s : 9
    ans = ans * 10 + x
    s -= x
  end
  ans
end
