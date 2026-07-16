# LeetCode 0217 - Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
  seen = {}
  nums.any? do |num|
    return true if seen.key?(num)

    seen[num] = true
    false
  end
end
