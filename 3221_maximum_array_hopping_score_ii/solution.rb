# LeetCode 3221 - Maximum Array Hopping Score II
# https://leetcode.com/problems/maximum-array-hopping-score-ii/

# @param {Integer[]} nums
# @return {Integer}
def max_score(nums)
  stk = []
  nums.each_index do |i|
    stk.pop while !stk.empty? && nums[stk[-1]] <= nums[i]
    stk << i
  end
  ans = 0
  cur = 0
  stk.each do |j|
    ans += (j - cur) * nums[j]
    cur = j
  end
  ans
end
