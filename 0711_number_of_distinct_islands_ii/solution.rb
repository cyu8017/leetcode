# LeetCode 0711 - Number of Distinct Islands II
# https://leetcode.com/problems/number-of-distinct-islands-ii/

# @param {Integer[][]} grid
# @return {Integer}
def num_distinct_islands2(grid)
  return 0 if grid.nil? || grid.empty?

  m = grid.length
  n = grid[0].length
  shapes = {}

  dfs = lambda do |r, c, cells|
    return if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0

    grid[r][c] = 0
    cells << [r, c]
    [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
      dfs.call(r + dr, c + dc, cells)
    end
  end

  transforms = [
    ->(x, y) { [x, y] },
    ->(x, y) { [x, -y] },
    ->(x, y) { [-x, y] },
    ->(x, y) { [-x, -y] },
    ->(x, y) { [y, x] },
    ->(x, y) { [y, -x] },
    ->(x, y) { [-y, x] },
    ->(x, y) { [-y, -x] }
  ]

  canonical = lambda do |cells|
    norms = transforms.map do |transform|
      pts = cells.map { |x, y| transform.call(x, y) }
      min_x = pts.map(&:first).min
      min_y = pts.map(&:last).min
      pts.map { |p| [p[0] - min_x, p[1] - min_y] }.sort
    end
    norms.min
  end

  m.times do |i|
    n.times do |j|
      next unless grid[i][j] == 1

      cells = []
      dfs.call(i, j, cells)
      shapes[canonical.call(cells)] = true
    end
  end
  shapes.length
end
