# LeetCode 0315 - Count of Smaller Numbers After Self
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution
  def countSmaller(nums)
    sorted_nums = []
    result = []
    nums.reverse_each do |num|
      index = bisect_left(sorted_nums, num)
      result << index
      sorted_nums.insert(index, num)
    end
    result.reverse
  end

  private

  def bisect_left(arr, num)
    left = 0
    right = arr.length
    while left < right
      mid = (left + right) / 2
      if arr[mid] < num
        left = mid + 1
      else
        right = mid
      end
    end
    left
  end
end
