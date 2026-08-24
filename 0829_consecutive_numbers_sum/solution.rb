# LeetCode 0829 - Consecutive Numbers Sum
# https://leetcode.com/problems/consecutive-numbers-sum/

# @param {Integer} n
# @return {Integer}
def consecutive_numbers_sum(n)
  ans = 0
  k = 1
  while k * (k - 1) / 2 < n
    ans += 1 if (n - k * (k - 1) / 2) % k == 0
    k += 1
  end
  ans
end
