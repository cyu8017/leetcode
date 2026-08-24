# LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
# https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def minimum_total_cost(nums1, nums2)
  n = nums1.length
  freq = Hash.new(0)
  ans = 0
  same = 0
  (0...n).each do |i|
    next unless nums1[i] == nums2[i]

    same += 1
    freq[nums1[i]] += 1
    ans += i
  end
  max_freq = 0
  max_val = 0
  freq.each do |key, value|
    if value > max_freq
      max_freq = value
      max_val = key
    end
  end
  need = max_freq * 2 - same
  return ans if need <= 0

  i = 0
  while i < n && need > 0
    if nums1[i] != nums2[i] && nums1[i] != max_val && nums2[i] != max_val
      ans += i
      need -= 1
    end
    i += 1
  end
  need > 0 ? -1 : ans
end
