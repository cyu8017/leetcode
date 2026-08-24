# LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_subarray_sum(nums, k)
  n = nums.length
  pref = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] + nums[i] }
  inf = 9_007_199_254_740_991
  best = Array.new(k, inf)
  best[0] = 0
  ans = -inf
  (1..n).each do |i|
    r = i % k
    if best[r] != inf
      cand = pref[i] - best[r]
      ans = cand if cand > ans
    end
    best[r] = pref[i] if pref[i] < best[r]
  end
  ans
end
