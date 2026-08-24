# LeetCode 3341 - Find Minimum Time to Reach Last Room I
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

# @param {Integer[][]} move_time
# @return {Integer}
def min_time_to_reach(move_time)
  m = move_time.length
  n = move_time[0].length
  dist = Array.new(m) { Array.new(n, 1 << 30) }
  h = [[0, 0, 0]]
  dist[0][0] = 0
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  until h.empty?
    h.sort_by! { |a| a[0] }
    t, r, c = h.shift
    next if t != dist[r][c]
    return t if r == m - 1 && c == n - 1

    dirs.each do |d|
      nr = r + d[0]
      nc = c + d[1]
      next if nr < 0 || nc < 0 || nr >= m || nc >= n

      start = [t, move_time[nr][nc]].max
      nt = start + 1
      if nt < dist[nr][nc]
        dist[nr][nc] = nt
        h << [nt, nr, nc]
      end
    end
  end
  -1
end
