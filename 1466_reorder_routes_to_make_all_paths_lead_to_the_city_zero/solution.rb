# LeetCode 1466 - Reorder Routes To Make All Paths Lead To The City Zero
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

def min_reorder(n, connections)
  graph = Array.new(n) { [] }
  connections.each do |a, b|
    graph[a] << [b, 1]
    graph[b] << [a, 0]
  end
  ans = 0
  stack = [0]
  seen = { 0 => true }
  until stack.empty?
    node = stack.pop
    graph[node].each do |nei, cost|
      next if seen[nei]
      seen[nei] = true
      stack << nei
      ans += cost
    end
  end
  ans
end
