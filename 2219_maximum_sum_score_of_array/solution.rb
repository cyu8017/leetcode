# LeetCode 2219 - Maximum Sum Score of Array
# https://leetcode.com/problems/maximum-sum-score-of-array/

# @param {Integer[]} nums
# @return {Integer}
def maximum_sum_score(nums)
  total = nums.sum
  pref = 0
  ans = -Float::INFINITY
  nums.each do |x|
    pref += x
    ans = [ans, pref, total - pref + x].max
  end
  ans.to_i
end

alias solve maximum_sum_score
