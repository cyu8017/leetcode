# LeetCode 3524 - Find X Value of Array I
# https://leetcode.com/problems/find-x-value-of-array-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def result_array(nums, k)
  ans = Array.new(k, 0)
  dp = Array.new(k, 0)
  nums.each do |num|
    new_dp = Array.new(k, 0)
    nm = num % k
    new_dp[nm] = 1
    (0...k).each { |i| new_dp[(i * nm) % k] += dp[i] }
    (0...k).each { |i| ans[i] += new_dp[i] }
    dp = new_dp
  end
  ans
end
