# LeetCode 0473 - Matchsticks to Square
# https://leetcode.com/problems/matchsticks-to-square/

class Solution
  def makesquare(matchsticks)
    return false if matchsticks.empty?

    total = matchsticks.sum
    return false if total % 4 != 0

    side = total / 4
    sorted = matchsticks.sort.reverse

    dfs = lambda do |index, sides|
      return sides[0] == side && sides.uniq.length == 1 if index == sorted.length

      length = sorted[index]
      (0...4).each do |side_index|
        next if sides[side_index] + length > side
        next if side_index.positive? && sides[side_index] == sides[side_index - 1]

        sides[side_index] += length
        return true if dfs.call(index + 1, sides)
        sides[side_index] -= length
      end
      false
    end

    dfs.call(0, [0, 0, 0, 0])
  end
end
