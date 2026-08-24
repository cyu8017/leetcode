# LeetCode 0611 - Valid Triangle Number
# https://leetcode.com/problems/valid-triangle-number/

# @param {Integer[]} nums
# @return {Integer}
def triangle_number(nums)
  nums.sort!
  n = nums.length
  count = 0

  (n - 1).downto(2) do |k|
    left = 0
    right = k - 1
    while left < right
      if nums[left] + nums[right] > nums[k]
        count += right - left
        right -= 1
      else
        left += 1
      end
    end
  end

  count
end
