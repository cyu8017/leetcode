# LeetCode 0200 - Number of Islands
class Solution
  def num_islands(grid)
    return 0 if grid.empty?

    rows = grid.length
    cols = grid[0].length
    count = 0

    dfs = lambda do |row, col|
      return if row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] != "1"

      grid[row][col] = "0"
      dfs.call(row + 1, col)
      dfs.call(row - 1, col)
      dfs.call(row, col + 1)
      dfs.call(row, col - 1)
    end

    rows.times do |row|
      cols.times do |col|
        next unless grid[row][col] == "1"

        count += 1
        dfs.call(row, col)
      end
    end
    count
  end
end