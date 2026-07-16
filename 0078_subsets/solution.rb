# LeetCode 0078 - Subsets
# https://leetcode.com/problems/subsets/

# @param {Integer[]} nums
# @return {Integer[][]}
def subsets(nums)
  result = [[]]

  nums.each do |num|
    size = result.length
    (0...size).each do |i|
      result << result[i] + [num]
    end
  end

  result
end
