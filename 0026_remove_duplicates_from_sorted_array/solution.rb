# LeetCode 0026 - Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
  return 0 if nums.empty?

  write = 1
  (1...nums.length).each do |read|
    if nums[read] != nums[write - 1]
      nums[write] = nums[read]
      write += 1
    end
  end
  write
end
