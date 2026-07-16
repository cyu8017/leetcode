# LeetCode 0350 - Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution
  def intersect(nums1, nums2)
    counts = Hash.new(0)
    nums1.each { |num| counts[num] += 1 }

    result = []
    nums2.each do |num|
      next unless counts[num] > 0

      result << num
      counts[num] -= 1
    end

    result
  end
end
