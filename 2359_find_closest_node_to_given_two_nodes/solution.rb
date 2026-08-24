# LeetCode 2359 - Find Closest Node to Given Two Nodes
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

# @param {Integer[]} edges
# @param {Integer} node1
# @param {Integer} node2
# @return {Integer}
def closest_meeting_node(edges, node1, node2)
  n = edges.length
  dist = lambda do |start|
    d = Array.new(n, -1)
    cur = start
    step = 0
    while cur != -1 && d[cur] == -1
      d[cur] = step
      cur = edges[cur]
      step += 1
    end
    d
  end
  d1 = dist.call(node1)
  d2 = dist.call(node2)
  ans = -1
  best = Float::INFINITY
  (0...n).each do |i|
    next if d1[i] == -1 || d2[i] == -1
    mx = [d1[i], d2[i]].max
    if mx < best
      best = mx
      ans = i
    end
  end
  ans
end
