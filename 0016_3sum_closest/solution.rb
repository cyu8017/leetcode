# LeetCode 0016 - 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def three_sum_closest(nums, target)
  nums.sort!
  closest = nums[0] + nums[1] + nums[2]

  (0...(nums.length - 2)).each do |i|
    left = i + 1
    right = nums.length - 1
    while left < right
      total = nums[i] + nums[left] + nums[right]
      closest = total if (total - target).abs < (closest - target).abs
      if total < target
        left += 1
      elsif total > target
        right -= 1
      else
        return total
      end
    end
  end

  closest
end
