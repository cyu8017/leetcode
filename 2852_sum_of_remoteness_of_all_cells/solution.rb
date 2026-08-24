# LeetCode 2852 - Sum of Remoteness of All Cells
# https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

# @param {Integer[][]} grid
# @return {Integer}
def sum_remoteness(grid)
  m = grid.length
  n = grid[0].length
  seen = Array.new(m) { Array.new(n, false) }
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  total = 0
  (0...m).each do |i|
    (0...n).each { |j| total += grid[i][j] if grid[i][j] != -1 }
  end
  ans = 0
  (0...m).each do |i|
    (0...n).each do |j|
      next if grid[i][j] == -1 || seen[i][j]

      q = [[i, j]]
      seen[i][j] = true
      sm = 0
      cnt = 0
      h = 0
      while h < q.length
        x, y = q[h]
        h += 1
        sm += grid[x][y]
        cnt += 1
        dirs.each do |dx, dy|
          ni = x + dx
          nj = y + dy
          if ni >= 0 && ni < m && nj >= 0 && nj < n && !seen[ni][nj] && grid[ni][nj] != -1
            seen[ni][nj] = true
            q << [ni, nj]
          end
        end
      end
      ans += (total - sm) * cnt
    end
  end
  ans
end
