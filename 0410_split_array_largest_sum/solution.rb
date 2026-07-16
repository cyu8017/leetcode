# LeetCode 0410 - Split Array Largest Sum
# https://leetcode.com/problems/split-array-largest-sum/

class Solution
  def split_array(nums, k)
    left = nums.max
    right = nums.sum

    while left < right
      mid = (left + right) / 2
      if can_split(nums, k, mid)
        right = mid
      else
        left = mid + 1
      end
    end

    left
  end

  alias_method :splitArray, :split_array

  private

  def can_split(nums, k, limit)
    parts = 1
    current = 0
    nums.each do |value|
      if current + value > limit
        parts += 1
        current = 0
      end
      current += value
    end
    parts <= k
  end
end
