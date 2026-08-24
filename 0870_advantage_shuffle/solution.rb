# LeetCode 0870 - Advantage Shuffle
# https://leetcode.com/problems/advantage-shuffle/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def advantage_count(nums1, nums2)
  sorted1 = nums1.sort
  ans = Array.new(nums1.length, 0)
  nums2.each_with_index.sort_by { |val, _| -val }.each do |val, i|
    ans[i] = sorted1[-1] > val ? sorted1.pop : sorted1.shift
  end
  ans
end
