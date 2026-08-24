# LeetCode 3151 - Special Array I
# https://leetcode.com/problems/special-array-i/

# @param {Integer[]} nums
# @return {Boolean}
def is_array_special(nums)
  (1...nums.length).each do |i|
    return false if nums[i] % 2 == nums[i - 1] % 2
  end
  true
end
