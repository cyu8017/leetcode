# LeetCode 0294 - Flip Game II
# https://leetcode.com/problems/flip-game-ii/

class Solution
  def canWin(current_state)
    memo = {}

    can_win = lambda do |state|
      return memo[state] if memo.key?(state)

      (0...(state.length - 1)).each do |index|
        next unless state[index, 2] == "++"

        next_state = state[0...index] + "--" + state[(index + 2)..]
        unless can_win.call(next_state)
          memo[state] = true
          return true
        end
      end
      memo[state] = false
      false
    end

    can_win.call(current_state)
  end
end
