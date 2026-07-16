# LeetCode 0390 - Elimination Game
# https://leetcode.com/problems/elimination-game/

class Solution
  def last_remaining(n)
    left = 1
    right = n
    step = 1
    remaining = n
    from_left = true

    while left < right
      left += step if from_left || remaining.odd?
      right -= step
      step *= 2
      remaining /= 2
      from_left = !from_left
    end

    left
  end

  alias_method :lastRemaining, :last_remaining
end
