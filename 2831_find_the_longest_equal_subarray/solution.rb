# LeetCode 2831 - Find the Longest Equal Subarray
# https://leetcode.com/problems/find-the-longest-equal-subarray/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def longest_equal_subarray(nums, k)
  pos = {}
  nums.each_with_index { |v, i| (pos[v] ||= []) << i }
  ans = 0
  pos.each_value do |p|
    left = 0
    p.each_index do |right|
      left += 1 while p[right] - p[left] - (right - left) > k
      ans = [ans, right - left + 1].max
    end
  end
  ans
end
