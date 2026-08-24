# LeetCode 3686 - Number of Stable Subsequences
# https://leetcode.com/problems/number-of-stable-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def count_stable_subsequences(nums)
  mod = 1_000_000_007
  a1 = a2 = b1 = b2 = 0
  nums.each do |x|
    if x.odd?
      na1 = (1 + b1 + b2) % mod
      na2 = a1
      a1 = (a1 + na1) % mod
      a2 = (a2 + na2) % mod
    else
      nb1 = (1 + a1 + a2) % mod
      nb2 = b1
      b1 = (b1 + nb1) % mod
      b2 = (b2 + nb2) % mod
    end
  end
  (((a1 + a2) % mod + b1) % mod + b2) % mod
end
