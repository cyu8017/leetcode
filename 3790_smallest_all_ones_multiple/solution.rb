# LeetCode 3790 - Smallest All Ones Multiple
# https://leetcode.com/problems/smallest-all-ones-multiple/

# @param {Integer} k
# @return {Integer}
def min_all_one_multiple(k)
  return -1 if (k & 1) == 0
  x = 1 % k
  ans = 1
  k.times do
    x = (x * 10 + 1) % k
    ans += 1
    return ans if x == 0
  end
  -1
end
