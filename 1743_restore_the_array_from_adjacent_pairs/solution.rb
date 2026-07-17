# LeetCode 1743 - Restore the Array From Adjacent Pairs
# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

# @param {Integer[][]} adjacent_pairs
# @return {Integer[]}
def restore_array(adjacent_pairs)
  graph = Hash.new { |hash, key| hash[key] = [] }
  adjacent_pairs.each do |a, b|
    graph[a] << b
    graph[b] << a
  end
  start = graph.find { |_, neighbors| neighbors.length == 1 }[0]
  ans = [start]
  prev = nil
  while ans.length < graph.length
    cur = ans[-1]
    neighbors = graph[cur]
    nxt = neighbors[0] != prev ? neighbors[0] : neighbors[1]
    ans << nxt
    prev = cur
  end
  ans
end
