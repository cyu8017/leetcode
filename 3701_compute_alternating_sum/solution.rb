# LeetCode 3701 - Compute Alternating Sum
# https://leetcode.com/problems/compute-alternating-sum/

# @param {Integer[]} nums
# @return {Integer}
def alternating_sum(nums)
  ans = 0
  nums.each_with_index { |x, i| ans += i.even? ? x : -x }
  ans
end
