# LeetCode 0896 - Monotonic Array
# https://leetcode.com/problems/monotonic-array/

# @param {Integer[]} nums
# @return {Boolean}
def is_monotonic(nums)
  inc = dec = true
  (1...nums.length).each do |i|
    inc = false if nums[i] < nums[i - 1]
    dec = false if nums[i] > nums[i - 1]
  end
  inc || dec
end
