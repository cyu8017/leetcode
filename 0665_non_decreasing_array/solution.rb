# LeetCode 0665 - Non-decreasing Array
# https://leetcode.com/problems/non-decreasing-array/

# @param {Integer[]} nums
# @return {Boolean}
def check_possibility(nums)
  changed = false
  (1...nums.length).each do |i|
    next if nums[i] >= nums[i - 1]
    return false if changed

    changed = true
    if i >= 2 && nums[i] < nums[i - 2]
      nums[i] = nums[i - 1]
    else
      nums[i - 1] = nums[i]
    end
  end
  true
end
