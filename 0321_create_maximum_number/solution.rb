# LeetCode 0321 - Create Maximum Number
# https://leetcode.com/problems/create-maximum-number/

class Solution
  def maxNumber(nums1, nums2, k)
    pick_max = lambda do |values, count|
      drop = values.length - count
      stack = []
      values.each do |value|
        while drop > 0 && !stack.empty? && stack[-1] < value
          stack.pop
          drop -= 1
        end
        stack << value
      end
      stack[0, count]
    end

    merge = lambda do |first, second|
      result = []
      left = 0
      right = 0
      while left < first.length && right < second.length
        if first[left..-1] > second[right..-1]
          result << first[left]
          left += 1
        else
          result << second[right]
          right += 1
        end
      end
      result.concat(first[left..-1] || [])
      result.concat(second[right..-1] || [])
      result
    end

    best = []
    start_take = [0, k - nums2.length].max
    end_take = [k, nums1.length].min
    (start_take..end_take).each do |take_first|
      take_second = k - take_first
      candidate = merge.call(pick_max.call(nums1, take_first), pick_max.call(nums2, take_second))
      best = candidate if candidate > best
    end
    best
  end
end
