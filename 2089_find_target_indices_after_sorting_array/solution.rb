# LeetCode 2089 - Find Target Indices After Sorting Array
# https://leetcode.com/problems/find-target-indices-after-sorting-array/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def target_indices(nums, target)
  less = eq = 0
  nums.each do |x|
    if x < target
      less += 1
    elsif x == target
      eq += 1
    end
  end
  (0...eq).map { |i| less + i }
end
