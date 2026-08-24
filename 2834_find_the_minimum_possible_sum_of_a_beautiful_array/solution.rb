# LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
# https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

# @param {Integer} n
# @param {Integer} target
# @return {Integer}
def minimum_possible_sum(n, target)
  mod = 1_000_000_007
  m = target / 2
  return (n * (n + 1) / 2) % mod if n <= m

  total = m * (m + 1) / 2
  remain = n - m
  total += remain * target + remain * (remain - 1) / 2
  total % mod
end
