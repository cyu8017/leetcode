# LeetCode 2123 - Minimum Operations to Remove Adjacent Ones in Matrix
# https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_operations(grid)
  m = grid.length
  n = grid[0].length
  ids = Array.new(m) { Array.new(n, -1) }
  cnt = 0
  m.times do |i|
    n.times do |j|
      if grid[i][j] == 1
        ids[i][j] = cnt
        cnt += 1
      end
    end
  end
  g = Array.new(cnt) { [] }
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  m.times do |i|
    n.times do |j|
      next if grid[i][j] != 1 || (i + j).odd?

      u = ids[i][j]
      dirs.each do |di, dj|
        ni = i + di
        nj = j + dj
        g[u] << ids[ni][nj] if ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1
      end
    end
  end
  match = Array.new(cnt, -1)
  dfs = nil
  dfs = lambda do |u, seen|
    g[u].each do |v|
      next if seen[v]

      seen[v] = true
      if match[v] == -1 || dfs.call(match[v], seen)
        match[v] = u
        return true
      end
    end
    false
  end

  ans = 0
  cnt.times do |u|
    ok = false
    i = 0
    while i < m && !ok
      n.times do |j|
        if ids[i][j] == u && (i + j).even?
          ok = true
          break
        end
      end
      i += 1
    end
    next unless ok

    seen = Array.new(cnt, false)
    ans += 1 if dfs.call(u, seen)
  end
  ans
end
