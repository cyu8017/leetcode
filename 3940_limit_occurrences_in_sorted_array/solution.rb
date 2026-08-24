# LeetCode 3940 - Limit Occurrences In Sorted Array
# https://leetcode.com/problems/limit-occurrences-in-sorted-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def limit_occurrences(nums, k)
  n = nums.length
  cnt = 1
  l = 1
  (1...n).each do |r|
    if nums[r] != nums[r - 1]
      cnt = 1
    else
      cnt += 1
    end
    if cnt <= k
      nums[l] = nums[r]
      l += 1
    end
  end
  nums[0...l]
end
