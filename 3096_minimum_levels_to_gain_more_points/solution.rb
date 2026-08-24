# LeetCode 3096 - Minimum Levels to Gain More Points
# https://leetcode.com/problems/minimum-levels-to-gain-more-points/

# @param {Integer[]} possible
# @return {Integer}
def minimum_levels(possible)
  s = possible.sum { |x| x == 0 ? -1 : x }
  t = 0
  (0...possible.length - 1).each do |i|
    x = possible[i] == 0 ? -1 : possible[i]
    t += x
    return i + 1 if t > s - t
  end
  -1
end
