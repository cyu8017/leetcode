# LeetCode 2103 - Rings and Rods
# https://leetcode.com/problems/rings-and-rods/

# @param {String} rings
# @return {Integer}
def count_points(rings)
  mask = Array.new(10, 0)
  0.step(rings.length - 1, 2) do |i|
    c = rings[i]
    r = rings[i + 1].ord - 48
    bit = c == "R" ? 1 : c == "G" ? 2 : 4
    mask[r] |= bit
  end
  mask.count { |m| m == 7 }
end
