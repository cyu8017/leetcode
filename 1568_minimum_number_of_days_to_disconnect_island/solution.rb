# LeetCode 1568 - Minimum Number of Days to Disconnect Island
# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

# @param {Integer[][]} grid
# @return {Integer}
def min_days(grid)
  m = grid.length
  n = grid[0].length
  islands = lambda do
    seen = {}
    count = 0
    (0...m).each do |r|
      (0...n).each do |c|
        next unless grid[r][c] == 1 && !seen[[r, c]]
        count += 1
        stack = [[r, c]]
        seen[[r, c]] = true
        until stack.empty?
          x, y = stack.pop
          [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dx, dy|
            nx = x + dx
            ny = y + dy
            next unless nx.between?(0, m - 1) && ny.between?(0, n - 1)
            next unless grid[nx][ny] == 1 && !seen[[nx, ny]]
            seen[[nx, ny]] = true
            stack << [nx, ny]
          end
        end
      end
    end
    count
  end
  return 0 if islands.call != 1
  (0...m).each do |r|
    (0...n).each do |c|
      next unless grid[r][c] == 1
      grid[r][c] = 0
      if islands.call != 1
        grid[r][c] = 1
        return 1
      end
      grid[r][c] = 1
    end
  end
  2
end
