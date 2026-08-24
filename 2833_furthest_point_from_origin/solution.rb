# LeetCode 2833 - Furthest Point From Origin
# https://leetcode.com/problems/furthest-point-from-origin/

# @param {String} moves
# @return {Integer}
def furthest_distance_from_origin(moves)
  left = right = u = 0
  moves.each_char do |c|
    if c == "L"
      left += 1
    elsif c == "R"
      right += 1
    else
      u += 1
    end
  end
  (left - right).abs + u
end
