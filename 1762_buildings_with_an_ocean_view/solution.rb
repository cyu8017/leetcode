# LeetCode 1762 - Buildings With an Ocean View
# https://leetcode.com/problems/buildings-with-an-ocean-view/

# @param {Integer[]} heights
# @return {Integer[]}
def find_buildings(heights)
  ans = []
  tallest = 0
  (heights.length - 1).downto(0) do |i|
    if heights[i] > tallest
      ans << i
      tallest = heights[i]
    end
  end
  ans.reverse
end
