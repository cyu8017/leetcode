# LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_swap(nums1, nums2)
  n = nums1.length
  swap = Array.new(n, n)
  keep = Array.new(n, n)
  swap[0] = 1
  keep[0] = 0
  (1...n).each do |i|
    if nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]
      keep[i] = keep[i - 1]
      swap[i] = swap[i - 1] + 1
    end
    if nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]
      keep[i] = [keep[i], swap[i - 1]].min
      swap[i] = [swap[i], keep[i - 1] + 1].min
    end
  end
  [swap[-1], keep[-1]].min
end
