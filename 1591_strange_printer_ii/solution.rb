# LeetCode 1591 - Strange Printer II
# https://leetcode.com/problems/strange-printer-ii/

# @param {Integer[][]} target_grid
# @return {Boolean}
def is_printable(target_grid)
  colors = {}
  target_grid.each { |row| row.each { |x| colors[x] = true } }
  bounds = {}
  colors.each_key { |c| bounds[c] = [10**9, 10**9, -1, -1] }
  target_grid.each_with_index do |row, r|
    row.each_with_index do |c, col|
      b = bounds[c]
      b[0] = [b[0], r].min
      b[1] = [b[1], col].min
      b[2] = [b[2], r].max
      b[3] = [b[3], col].max
    end
  end
  graph = Hash.new { |h, k| h[k] = {} }
  indegree = colors.keys.to_h { |c| [c, 0] }
  bounds.each do |c, (r1, c1, r2, c2)|
    (r1..r2).each do |r|
      (c1..c2).each do |col|
        other = target_grid[r][col]
        next if other == c || graph[c][other]
        graph[c][other] = true
        indegree[other] += 1
      end
    end
  end
  queue = colors.keys.select { |c| indegree[c].zero? }
  seen = 0
  until queue.empty?
    c = queue.shift
    seen += 1
    graph[c].each_key do |nxt|
      indegree[nxt] -= 1
      queue << nxt if indegree[nxt].zero?
    end
  end
  seen == colors.length
end
