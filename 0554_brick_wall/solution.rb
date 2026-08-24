# LeetCode 0554 - Brick Wall
# https://leetcode.com/problems/brick-wall/

# @param {Integer[][]} wall
# @return {Integer}
def least_bricks(wall)
  edges = Hash.new(0)
  wall.each do |row|
    width = 0
    row[0...-1].each do |brick|
      width += brick
      edges[width] += 1
    end
  end
  wall.length - (edges.empty? ? 0 : edges.values.max)
end
