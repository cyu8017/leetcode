# LeetCode 0349 - Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution
  def intersection(nums1, nums2)
    set2 = {}
    nums2.each { |num| set2[num] = true }
    seen = {}
    result = []

    nums1.each do |num|
      next unless set2[num] && !seen[num]

      seen[num] = true
      result << num
    end

    result
  end
end
