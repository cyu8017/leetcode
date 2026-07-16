# LeetCode 0259 - 3Sum Smaller
# https://leetcode.com/problems/3sum-smaller/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def three_sum_smaller(nums, target)
  sorted = nums.sort
  count = 0
  (0...(sorted.length - 2)).each do |index|
    left = index + 1
    right = sorted.length - 1
    while left < right
      total = sorted[index] + sorted[left] + sorted[right]
      if total < target
        count += right - left
        left += 1
      else
        right -= 1
      end
    end
  end
  count
end
