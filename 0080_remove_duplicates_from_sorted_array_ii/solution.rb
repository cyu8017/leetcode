# LeetCode 0080 - Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
  return nums.length if nums.length <= 2

  write = 2
  (2...nums.length).each do |i|
    if nums[i] != nums[write - 2]
      nums[write] = nums[i]
      write += 1
    end
  end
  write
end
