# LeetCode 0416 - Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

require "set"

class Solution
  def can_partition(nums)
    total = nums.sum
    return false if total.odd?

    target = total / 2
    possible = Set[0]

    nums.each do |value|
      possible = possible | possible.filter_map { |amount| amount + value if amount + value <= target }.to_set
      return true if possible.include?(target)
    end

    possible.include?(target)
  end

  alias_method :canPartition, :can_partition
end
