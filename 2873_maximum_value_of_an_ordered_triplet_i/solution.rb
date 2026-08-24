# LeetCode 2873 - Maximum Value of an Ordered Triplet I
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

# @param {Integer[]} nums
# @return {Integer}
def maximum_triplet_value(nums)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    (i + 1...n).each do |j|
      (j + 1...n).each do |k|
        cand = (nums[i] - nums[j]) * nums[k]
        ans = cand if cand > ans
      end
    end
  end
  ans
end
