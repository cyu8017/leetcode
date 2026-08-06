# LeetCode 1909 - Remove One Element to Make the Array Strictly Increasing
# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

# @param {Integer[]} nums
# @return {Boolean}
def can_be_increasing(nums)
  check = lambda do |skip|
    prev = nil
    nums.each_with_index do |x, i|
      next if i == skip
      return false if !prev.nil? && x <= prev
      prev = x
    end
    true
  end
  (1...nums.length).each do |i|
    return check.call(i - 1) || check.call(i) if nums[i] <= nums[i - 1]
  end
  true
end
