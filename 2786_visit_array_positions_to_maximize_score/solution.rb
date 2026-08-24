# LeetCode 2786 - Visit Array Positions to Maximize Score
# https://leetcode.com/problems/visit-array-positions-to-maximize-score/

# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def max_score(nums, x)
  neg = -10**18
  even = odd = nums[0]
  if nums[0].even?
    odd = neg
  else
    even = neg
  end
  (1...nums.length).each do |i|
    v = nums[i]
    if v.even?
      even = [even + v, odd + v - x].max
    else
      odd = [odd + v, even + v - x].max
    end
  end
  [even, odd].max
end
