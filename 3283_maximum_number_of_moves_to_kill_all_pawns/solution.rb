# LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
# https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

# @param {Integer} kx
# @param {Integer} ky
# @param {Integer[][]} positions
# @return {Integer}
def max_moves(kx, ky, positions)
  dirs = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
  knight_dist = lambda do |x, y, pts|
    np = pts.length
    ans = Array.new(np, -1)
    vis = Array.new(50) { Array.new(50, false) }
    q = [[x, y, 0]]
    vis[x][y] = true
    need = {}
    (0...np).each do |i|
      key = (pts[i][0] << 32) | (pts[i][1] & 0xFFFFFFFF)
      need[key] ||= []
      need[key] << i
    end
    found = 0
    while !q.empty? && found < np
      cur = q.shift
      key = (cur[0] << 32) | (cur[1] & 0xFFFFFFFF)
      idxs = need[key]
      if idxs
        idxs.each do |i|
          if ans[i] == -1
            ans[i] = cur[2]
            found += 1
          end
        end
      end
      dirs.each do |d|
        nx = cur[0] + d[0]
        ny = cur[1] + d[1]
        next if nx < 0 || ny < 0 || nx >= 50 || ny >= 50 || vis[nx][ny]
        vis[nx][ny] = true
        q << [nx, ny, cur[2] + 1]
      end
    end
    ans
  end
  n = positions.length
  pts = Array.new(n + 1) { [0, 0] }
  pts[0][0] = kx
  pts[0][1] = ky
  (0...n).each do |i|
    pts[i + 1][0] = positions[i][0]
    pts[i + 1][1] = positions[i][1]
  end
  dist = (0..n).map { |i| knight_dist.call(pts[i][0], pts[i][1], pts) }
  nn = 1 << n
  memo = Array.new(nn) { Array.new(n + 1, -1) }
  dfs = nil
  dfs = lambda do |mask, cur, turn|
    return 0 if mask == nn - 1
    return memo[mask][cur] if memo[mask][cur] != -1
    best = turn == 0 ? -(1 << 30) : (1 << 30)
    (0...n).each do |i|
      next if (mask & (1 << i)) != 0
      d = dist[cur][i + 1]
      v = d + dfs.call(mask | (1 << i), i + 1, 1 - turn)
      if turn == 0
        best = v if v > best
      elsif v < best
        best = v
      end
    end
    memo[mask][cur] = best
  end
  dfs.call(0, 0, 0)
end
