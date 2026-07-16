# LeetCode 0325 - Maximum Size Subarray Sum Equals k
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

class Solution
  def maxSubArrayLen(nums, k)
    prefix_index = { 0 => -1 }
    prefix = 0
    best = 0
    nums.each_with_index do |num, index|
      prefix += num
      if prefix_index.key?(prefix - k)
        best = [best, index - prefix_index[prefix - k]].max
      end
      prefix_index[prefix] = index unless prefix_index.key?(prefix)
    end
    best
  end
end
