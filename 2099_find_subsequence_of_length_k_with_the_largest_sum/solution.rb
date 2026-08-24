# LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def max_subsequence(nums, k)
  arr = nums.each_with_index.map { |v, i| [v, i] }
  arr.sort_by! { |v, _| -v }
  idx = arr[0...k].map { |_, i| i }.sort
  idx.map { |i| nums[i] }
end
