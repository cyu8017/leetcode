# LeetCode 3247 - Number of Subsequences with Odd Sum
# https://leetcode.com/problems/number-of-subsequences-with-odd-sum/

# @param {Integer[]} nums
# @return {Integer}
def subsequence_count(nums)
  mod = 1_000_000_007
  f = [0, 0]
  nums.each do |x|
    g = [0, 0]
    if x.odd?
      g[0] = (f[0] + f[1]) % mod
      g[1] = (f[0] + f[1] + 1) % mod
    else
      g[0] = (f[0] + f[0] + 1) % mod
      g[1] = (f[1] + f[1]) % mod
    end
    f = g
  end
  f[1]
end
