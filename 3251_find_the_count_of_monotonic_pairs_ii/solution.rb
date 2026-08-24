# LeetCode 3251 - Find the Count of Monotonic Pairs II
# https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

# @param {Integer[]} nums
# @return {Integer}
def count_of_pairs(nums)
  mod = 1_000_000_007
  n = nums.length
  max_v = nums.max
  dp = Array.new(max_v + 1, 0)
  (0..nums[0]).each { |a| dp[a] = 1 }
  (1...n).each do |i|
    ndp = Array.new(max_v + 1, 0)
    pref = Array.new(max_v + 2, 0)
    (0..max_v).each { |a| pref[a + 1] = (pref[a] + dp[a]) % mod }
    (0..nums[i]).each do |a2|
      b2 = nums[i] - a2
      max_a1 = a2
      lim = nums[i - 1] - b2
      max_a1 = lim if lim < max_a1
      next if max_a1 < 0
      max_a1 = max_v if max_a1 > max_v
      ndp[a2] = pref[max_a1 + 1]
    end
    dp = ndp
  end
  ans = 0
  dp.each { |v| ans = (ans + v) % mod }
  ans
end
