# LeetCode 3968 - Maximum Manhattan Distance After All Moves
# https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/

# @param {String} moves
# @return {Integer}
def max_distance(moves)
  x = 0
  y = 0
  z = 0
  moves.each_char do |c|
    case c
    when "U" then x -= 1
    when "D" then x += 1
    when "L" then y -= 1
    when "R" then y += 1
    else z += 1
    end
  end
  x.abs + y.abs + z
end
