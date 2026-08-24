# LeetCode 0912 - Sort an Array
# https://leetcode.com/problems/sort-an-array/

# @param {Integer[]} nums
# @return {Integer[]}
def sort_array(nums)
  return nums if nums.length <= 1

  mid = nums.length / 2
  left = sort_array(nums[0...mid])
  right = sort_array(nums[mid..])
  merged = []
  i = j = 0
  while i < left.length && j < right.length
    if left[i] <= right[j]
      merged << left[i]
      i += 1
    else
      merged << right[j]
      j += 1
    end
  end
  merged.concat(left[i..]) if i < left.length
  merged.concat(right[j..]) if j < right.length
  merged
end
