# LeetCode 2855 - Minimum Right Shifts to Sort the Array
# https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

# @param {Integer[]} nums
# @return {Integer}
def minimum_right_shifts(nums)
  n = nums.length
  drops = 0
  idx = -1
  (0...n).each do |i|
    if nums[i] > nums[(i + 1) % n]
      drops += 1
      idx = i
    end
  end
  return 0 if drops == 0
  return -1 if drops > 1

  n - 1 - idx
end
