# LeetCode 0546 - Remove Boxes
# https://leetcode.com/problems/remove-boxes/

class Solution
  def remove_boxes(boxes)
    memo = {}
    dp = lambda do |left, right, streak|
      return 0 if left > right

      key = [left, right, streak]
      return memo[key] if memo.key?(key)

      while right > left && boxes[right] == boxes[right - 1]
        right -= 1
        streak += 1
      end

      best = (streak + 1)**2 + dp.call(left, right - 1, 0)
      (left...right).each do |i|
        if boxes[i] == boxes[right]
          candidate = dp.call(left, i, streak + 1) + dp.call(i + 1, right - 1, 0)
          best = [best, candidate].max
        end
      end

      memo[key] = best
    end

    dp.call(0, boxes.length - 1, 0)
  end

  alias_method :removeBoxes, :remove_boxes
end
