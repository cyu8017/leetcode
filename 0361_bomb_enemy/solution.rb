# LeetCode 0361 - Bomb Enemy
# https://leetcode.com/problems/bomb-enemy/

class Solution
  def max_killed_enemies(grid)
    return 0 if grid.nil? || grid.empty? || grid[0].empty?

    rows = grid.length
    cols = grid[0].length
    row_hits = Array.new(rows) { Array.new(cols, 0) }
    col_hits = Array.new(rows) { Array.new(cols, 0) }

    rows.times do |row|
      count = 0
      cols.times do |col|
        if grid[row][col] == "W"
          count = 0
        elsif grid[row][col] == "E"
          count += 1
        else
          row_hits[row][col] = count
        end
      end

      count = 0
      (cols - 1).downto(0) do |col|
        if grid[row][col] == "W"
          count = 0
        elsif grid[row][col] == "E"
          count += 1
        else
          row_hits[row][col] += count
        end
      end
    end

    cols.times do |col|
      count = 0
      rows.times do |row|
        if grid[row][col] == "W"
          count = 0
        elsif grid[row][col] == "E"
          count += 1
        else
          col_hits[row][col] = count
        end
      end

      count = 0
      (rows - 1).downto(0) do |row|
        if grid[row][col] == "W"
          count = 0
        elsif grid[row][col] == "E"
          count += 1
        else
          col_hits[row][col] += count
        end
      end
    end

    best = 0
    rows.times do |row|
      cols.times do |col|
        best = [best, row_hits[row][col] + col_hits[row][col]].max
      end
    end
    best
  end

  alias_method :maxKilledEnemies, :max_killed_enemies
end
