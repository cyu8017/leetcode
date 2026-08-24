# LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  seen = {}
  nums.each { |x| seen[x] = true if x > 0 }
  seen.length
end
