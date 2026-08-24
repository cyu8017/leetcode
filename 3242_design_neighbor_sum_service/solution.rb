# LeetCode 3242 - Design Neighbor Sum Service
# https://leetcode.com/problems/design-neighbor-sum-service/

class NeighborSum
  def initialize(grid)
    @grid = grid
    @d = {}
    @dirs = [
      [-1, 0, 1, 0, -1],
      [-1, 1, 1, -1, -1]
    ]
    grid.each_with_index do |row, i|
      row.each_with_index { |v, j| @d[v] = [i, j] }
    end
  end

  def cal(value, k)
    p = @d[value]
    s = 0
    4.times do |q|
      x = p[0] + @dirs[k][q]
      y = p[1] + @dirs[k][q + 1]
      s += @grid[x][y] if x >= 0 && x < @grid.length && y >= 0 && y < @grid[0].length
    end
    s
  end

  def adjacent_sum(value)
    cal(value, 0)
  end

  def diagonal_sum(value)
    cal(value, 1)
  end
end
