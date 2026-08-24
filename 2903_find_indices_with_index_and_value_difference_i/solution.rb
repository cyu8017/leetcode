# LeetCode 2903 - Find Indices With Index and Value Difference I
# https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

# @param {Integer[]} nums
# @param {Integer} index_difference
# @param {Integer} value_difference
# @return {Integer[]}
def find_indices(nums, index_difference, value_difference)
  n = nums.length
  (0...n).each do |i|
    (i...n).each do |j|
      if (j - i).abs >= index_difference && (nums[i] - nums[j]).abs >= value_difference
        return [i, j]
      end
    end
  end
  [-1, -1]
end
