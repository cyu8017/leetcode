# LeetCode 2945 - Find Maximum Non-decreasing Array Length
# https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

# @param {Integer[]} nums
# @return {Integer}
def find_maximum_length(nums)
  n = nums.length
  pref = Array.new(n + 1, 0)
  last = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] + nums[i] }
  dp = Array.new(n + 1, 0)
  dq = [[0, 0]]
  (1..n).each do |i|
    dq.shift while dq.length > 1 && dq[1][1] <= pref[i]
    j = dq[0][0]
    dp[i] = dp[j] + 1
    last[i] = pref[i] - pref[j]
    val = pref[i] + last[i]
    dq.pop while !dq.empty? && dq[-1][1] >= val
    dq << [i, val]
  end
  dp[n]
end
