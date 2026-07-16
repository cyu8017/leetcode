# LeetCode 0525 - Contiguous Array
# https://leetcode.com/problems/contiguous-array/

class Solution
  def find_max_length(nums)
    counts = { 0 => -1 }
    balance = 0
    best = 0
    nums.each_with_index do |num, index|
      balance += num == 1 ? 1 : -1
      if counts.key?(balance)
        best = [best, index - counts[balance]].max
      else
        counts[balance] = index
      end
    end
    best
  end

  alias_method :findMaxLength, :find_max_length
end
