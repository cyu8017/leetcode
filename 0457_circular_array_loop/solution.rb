# LeetCode 0457 - Circular Array Loop
# https://leetcode.com/problems/circular-array-loop/

class Solution
  def circular_array_loop(nums)
    values = nums.dup
    length = values.length

    next_index = lambda do |index|
      (index + values[index]) % length
    end

    (0...length).each do |start|
      next if values[start] == 0

      forward = values[start] > 0
      slow = start
      fast = start

      loop do
        slow = next_index.call(slow)
        fast = next_index.call(next_index.call(fast))
        if values[slow] * (forward ? 1 : -1) <= 0 ||
           values[fast] * (forward ? 1 : -1) <= 0 ||
           values[next_index.call(fast)] * (forward ? 1 : -1) <= 0
          break
        elsif slow == fast
          return true if slow != next_index.call(slow)
          break
        end
      end

      index = start
      direction = values[start]
      while values[index] * direction > 0
        values[index] = 0
        index = next_index.call(index)
      end
    end

    false
  end

  alias_method :circularArrayLoop, :circular_array_loop
end
