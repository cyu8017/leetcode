# LeetCode 0480 - Sliding Window Median
# https://leetcode.com/problems/sliding-window-median/

class Solution
  def bisect_left(array, target)
    left = 0
    right = array.length
    while left < right
      mid = (left + right) / 2
      if array[mid] < target
        left = mid + 1
      else
        right = mid
      end
    end
    left
  end

  def median_sliding_window(nums, k)
    window = nums[0, k].sort
    result = []

    append_median = lambda do
      if k.odd?
        result << window[k / 2].to_f
      else
        result << (window[k / 2 - 1] + window[k / 2]) / 2.0
      end
    end

    append_median.call
    (k...nums.length).each do |index|
      outgoing = nums[index - k]
      incoming = nums[index]
      window.delete_at(bisect_left(window, outgoing))
      insert_at = bisect_left(window, incoming)
      window.insert(insert_at, incoming)
      append_median.call
    end
    result
  end

  alias_method :medianSlidingWindow, :median_sliding_window
end
