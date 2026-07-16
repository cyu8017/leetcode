# LeetCode 0523 - Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/

class Solution
  def check_subarray_sum(nums, k)
    prefix = 0
    remainders = { 0 => -1 }
    nums.each_with_index do |num, index|
      prefix += num
      mod = k.zero? ? prefix : prefix % k
      if remainders.key?(mod)
        return true if index - remainders[mod] >= 2
      else
        remainders[mod] = index
      end
    end
    false
  end

  alias_method :checkSubarraySum, :check_subarray_sum
end
