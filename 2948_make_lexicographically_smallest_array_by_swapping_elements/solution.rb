# LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

# @param {Integer[]} nums
# @param {Integer} limit
# @return {Integer[]}
def lexicographically_smallest_array(nums, limit)
  n = nums.length
  idx = (0...n).to_a
  idx.sort_by! { |i| nums[i] }
  ans = Array.new(n, 0)
  i = 0
  while i < n
    j = i + 1
    j += 1 while j < n && nums[idx[j]] - nums[idx[j - 1]] <= limit
    group_idx = idx[i...j].sort
    (j - i).times { |t| ans[group_idx[t]] = nums[idx[i + t]] }
    i = j
  end
  ans
end
