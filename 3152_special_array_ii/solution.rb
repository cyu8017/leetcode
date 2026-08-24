# LeetCode 3152 - Special Array II
# https://leetcode.com/problems/special-array-ii/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Boolean[]}
def is_array_special(nums, queries)
  n = nums.length
  d = (0...n).to_a
  (1...n).each { |i| d[i] = d[i - 1] if nums[i] % 2 != nums[i - 1] % 2 }
  queries.map { |q| d[q[1]] <= q[0] }
end
