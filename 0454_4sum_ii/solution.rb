# LeetCode 0454 - 4Sum II
# https://leetcode.com/problems/4sum-ii/

class Solution
  def four_sum_count(nums1, nums2, nums3, nums4)
    pair_sums = Hash.new(0)
    nums1.each do |a|
      nums2.each do |b|
        pair_sums[a + b] += 1
      end
    end

    total = 0
    nums3.each do |c|
      nums4.each do |d|
        total += pair_sums[-(c + d)]
      end
    end
    total
  end

  alias_method :fourSumCount, :four_sum_count
end
