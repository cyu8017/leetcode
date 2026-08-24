# LeetCode 3788 - Maximum Score of a Split
# https://leetcode.com/problems/maximum-score-of-a-split/

# @param {Integer[]} nums
# @return {Integer}
def maximum_score(nums)
  n = nums.length
  suf = Array.new(n, 0)
  suf[n - 1] = nums[n - 1]
  (n - 2).downto(0) { |i| suf[i] = [nums[i], suf[i + 1]].min }
  pre = 0
  ans = -(10**18)
  (0...(n - 1)).each do |i|
    pre += nums[i]
    ans = [ans, pre - suf[i + 1]].max
  end
  ans
end
