# LeetCode 0219 - Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def contains_nearby_duplicate(nums, k)
  last_index = {}
  nums.each_with_index do |num, i|
    return true if last_index.key?(num) && i - last_index[num] <= k

    last_index[num] = i
  end
  false
end
