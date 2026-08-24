# LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_max_sums(nums, k)
  mod = 1_000_000_007
  nums = nums.sort
  n = nums.length
  c = Array.new(n + 1) { Array.new(k, 0) }
  (0..n).each do |i|
    c[i][0] = 1
    j = 1
    while j < k && j <= i
      c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % mod
      j += 1
    end
  end
  ans = 0
  (0...n).each do |i|
    ways_max = 0
    j = 0
    while j < k && j <= i
      ways_max = (ways_max + c[i][j]) % mod
      j += 1
    end
    ways_min = 0
    right = n - i - 1
    j = 0
    while j < k && j <= right
      ways_min = (ways_min + c[right][j]) % mod
      j += 1
    end
    ans = (ans + nums[i] * ways_max % mod + nums[i] * ways_min % mod) % mod
  end
  ans
end
