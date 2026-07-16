# LeetCode 0293 - Flip Game
# https://leetcode.com/problems/flip-game/

class Solution
  def generatePossibleNextMoves(current_state)
    result = []
    (0...(current_state.length - 1)).each do |index|
      next unless current_state[index, 2] == "++"

      result << current_state[0...index] + "--" + current_state[(index + 2)..]
    end
    result
  end
end
