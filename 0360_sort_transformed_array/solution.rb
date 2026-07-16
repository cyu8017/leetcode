# LeetCode 0360 - Sort Transformed Array
# https://leetcode.com/problems/sort-transformed-array/

class Solution
  def sort_transformed_array(nums, a, b, c)
    transform = lambda do |value|
      a * value * value + b * value + c
    end

    left = 0
    right = nums.length - 1
    result = Array.new(nums.length)
    index = a > 0 ? nums.length - 1 : 0
    step = a > 0 ? -1 : 1

    while left <= right
      left_value = transform.call(nums[left])
      right_value = transform.call(nums[right])

      if a > 0
        if left_value > right_value
          result[index] = left_value
          left += 1
        else
          result[index] = right_value
          right -= 1
        end
      elsif left_value < right_value
        result[index] = left_value
        left += 1
      else
        result[index] = right_value
        right -= 1
      end

      index += step
    end

    result
  end

  alias_method :sortTransformedArray, :sort_transformed_array
end
