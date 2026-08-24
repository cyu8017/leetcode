# LeetCode 3819 - Rotate Non Negative Elements
# https://leetcode.com/problems/rotate-non-negative-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def rotate_elements(nums, k)
  t = nums.select { |x| x >= 0 }
  m = t.length
  return nums if m == 0
  d = Array.new(m, 0)
  (0...m).each { |i| d[((i - k) % m + m) % m] = t[i] }
  j = 0
  (0...nums.length).each do |i|
    if nums[i] >= 0
      nums[i] = d[j]
      j += 1
    end
  end
  nums
end
