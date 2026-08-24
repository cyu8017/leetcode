# LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
# https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

# @param {Integer[]} nums
# @return {Integer}
def max_selected_elements(nums)
  nums.sort!
  dp = Hash.new(0)
  ans = 0
  nums.each do |num|
    dn = dp[num]
    dnm1 = dp[num - 1]
    dp[num + 1] = dn + 1
    dp[num] = dnm1 + 1
    ans = [ans, dp[num], dp[num + 1]].max
  end
  ans
end
