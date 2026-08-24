# LeetCode 2619 - Array Prototype Last
# https://leetcode.com/problems/array-prototype-last/

# @param {Object[]} nums
# @return {Object}
def last(nums)
  return -1 if nums.empty?

  nums[-1]
end

alias solve last
