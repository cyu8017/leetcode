# LeetCode 2295 - Replace Elements in an Array
# https://leetcode.com/problems/replace-elements-in-an-array/

# @param {Integer[]} nums
# @param {Integer[][]} operations
# @return {Integer[]}
def array_change(nums, operations)
  pos = {}
  nums.each_with_index { |x, i| pos[x] = i }
  operations.each do |a, b|
    i = pos[a]
    nums[i] = b
    pos.delete(a)
    pos[b] = i
  end
  nums
end
