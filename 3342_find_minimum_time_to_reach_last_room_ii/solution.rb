# LeetCode 3342 - Find Minimum Time to Reach Last Room II
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

# @param {Integer[][]} move_time
# @return {Integer}
def min_time_to_reach(move_time)
  m = move_time.length
  n = move_time[0].length
  inf = 1 << 30
  dist = Array.new(m) { Array.new(n) { [inf, inf] } }
  pq = [[0, 0, 0, 0]]
  dist[0][0][0] = 0
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  until pq.empty?
    pq.sort_by! { |a| a[0] }
    t, r, c, parity = pq.shift
    next if t != dist[r][c][parity]
    return t if r == m - 1 && c == n - 1

    cost = parity == 1 ? 2 : 1
    dirs.each do |d|
      nr = r + d[0]
      nc = c + d[1]
      next if nr < 0 || nc < 0 || nr >= m || nc >= n

      start = [t, move_time[nr][nc]].max
      nt = start + cost
      np = 1 - parity
      if nt < dist[nr][nc][np]
        dist[nr][nc][np] = nt
        pq << [nt, nr, nc, np]
      end
    end
  end
  -1
end
