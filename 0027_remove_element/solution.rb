# LeetCode 0027 - Remove Element
# https://leetcode.com/problems/remove-element/

# @param {Integer[]} nums
# @param {Integer} val
# @return {Integer}
def remove_element(nums, val)
  write = 0
  nums.each do |num|
    if num != val
      nums[write] = num
      write += 1
    end
  end
  write
end
