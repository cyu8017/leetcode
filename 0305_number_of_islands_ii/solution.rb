# LeetCode 0305 - Number of Islands II
# https://leetcode.com/problems/number-of-islands-ii/

class Solution
  def numIslands2(m, n, positions)
    @parent = {}
    @rank = {}
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    result = []
    islands = 0

    positions.each do |row, col|
      index = row * n + col
      if @parent.key?(index)
        result << islands
        next
      end

      @parent[index] = index
      @rank[index] = 0
      islands += 1

      directions.each do |dr, dc|
        nr = row + dr
        nc = col + dc
        next unless nr >= 0 && nr < m && nc >= 0 && nc < n

        neighbor = nr * n + nc
        next unless @parent.key?(neighbor)
        next unless union(index, neighbor)

        islands -= 1
      end
      result << islands
    end
    result
  end

  private

  def find(index)
    @parent[index] = find(@parent[index]) if @parent[index] != index
    @parent[index]
  end

  def union(left, right)
    root_left = find(left)
    root_right = find(right)
    return false if root_left == root_right

    if @rank[root_left] < @rank[root_right]
      root_left, root_right = root_right, root_left
    end
    @parent[root_right] = root_left
    @rank[root_left] += 1 if @rank[root_left] == @rank[root_right]
    true
  end
end
