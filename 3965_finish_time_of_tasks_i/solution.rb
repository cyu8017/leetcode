# LeetCode 3965 - Finish Time Of Tasks I
# https://leetcode.com/problems/finish-time-of-tasks-i/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} base_time
# @return {Integer}
def finish_time(n, edges, base_time)
  g = Array.new(n) { [] }
  edges.each { |e| g[e[0]] << e[1] }
  dfs = nil
  dfs = lambda do |i|
    return base_time[i] if g[i].empty?
    inf = 1 << 62
    earliest = inf
    latest = -inf
    g[i].each do |j|
      a = dfs.call(j)
      earliest = a if a < earliest
      latest = a if a > latest
    end
    own_duration = (latest - earliest) + base_time[i]
    latest + own_duration
  end
  dfs.call(0)
end
