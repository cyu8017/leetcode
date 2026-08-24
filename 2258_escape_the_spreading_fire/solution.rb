# LeetCode 2258 - Escape the Spreading Fire
# https://leetcode.com/problems/escape-the-spreading-fire/

# @param {Integer[][]} grid
# @return {Integer}
def maximum_minutes(grid)
  m = grid.length
  n = grid[0].length
  inf = 1_000_000_000
  fire = Array.new(m) { Array.new(n, inf) }
  q = []
  m.times do |i|
    n.times do |j|
      if grid[i][j] == 1
        fire[i][j] = 0
        q << [i, j]
      end
    end
  end
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  until q.empty?
    r, c = q.shift
    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || fire[nr][nc] != inf

      fire[nr][nc] = fire[r][c] + 1
      q << [nr, nc]
    end
  end

  can = lambda do |wait|
    return false if wait >= fire[0][0]

    vis = Array.new(m) { Array.new(n, false) }
    qq = [[0, 0, wait]]
    vis[0][0] = true
    until qq.empty?
      r, c, t = qq.shift
      dirs.each do |dr, dc|
        nr = r + dr
        nc = c + dc
        nt = t + 1
        next if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || vis[nr][nc]

        if nr == m - 1 && nc == n - 1
          return true if nt <= fire[nr][nc]

          next
        end
        next if nt >= fire[nr][nc]

        vis[nr][nc] = true
        qq << [nr, nc, nt]
      end
    end
    false
  end

  lo = 0
  hi = m * n + 10
  ans = -1
  while lo <= hi
    mid = (lo + hi) >> 1
    if can.call(mid)
      ans = mid
      lo = mid + 1
    else
      hi = mid - 1
    end
  end
  ans >= m * n ? inf : ans
end
