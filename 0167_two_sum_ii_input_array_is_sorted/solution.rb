# LeetCode 0167 - Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution
  def two_sum(numbers, target)
    left = 0
    right = numbers.length - 1
    while left < right
      sum = numbers[left] + numbers[right]
      return [left + 1, right + 1] if sum == target

      sum < target ? left += 1 : right -= 1
    end
    []
  end
end