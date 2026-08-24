# LeetCode 3568 - Minimum Moves to Clean the Classroom
# https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

# @param {String[]} classroom
# @param {Integer} energy
# @return {Integer}
def min_moves(classroom, energy)
  m = classroom.length
  n = classroom[0].length
  d = Array.new(m) { Array.new(n, 0) }
  x = 0
  y = 0
  cnt = 0
  (0...m).each do |i|
    (0...n).each do |j|
      c = classroom[i][j]
      if c == "S"
        x = i
        y = j
      elsif c == "L"
        d[i][j] = cnt
        cnt += 1
      end
    end
  end
  return 0 if cnt == 0
  vis = Array.new(m) { Array.new(n) { Array.new(energy + 1) { Array.new(1 << cnt, false) } } }
  q = [[x, y, energy, (1 << cnt) - 1]]
  vis[x][y][energy][(1 << cnt) - 1] = true
  dirs = [-1, 0, 1, 0, -1]
  ans = 0
  until q.empty?
    t = q
    q = []
    t.each do |s|
      i, j, cur_energy, mask = s
      return ans if mask == 0
      next if cur_energy <= 0
      (0...4).each do |kk|
        nx = i + dirs[kk]
        ny = j + dirs[kk + 1]
        next unless nx >= 0 && nx < m && ny >= 0 && ny < n && classroom[nx][ny] != "X"
        nxt_energy = classroom[nx][ny] == "R" ? energy : cur_energy - 1
        nxt_mask = mask
        nxt_mask &= ~(1 << d[nx][ny]) if classroom[nx][ny] == "L"
        unless vis[nx][ny][nxt_energy][nxt_mask]
          vis[nx][ny][nxt_energy][nxt_mask] = true
          q << [nx, ny, nxt_energy, nxt_mask]
        end
      end
    end
    ans += 1
  end
  -1
end
