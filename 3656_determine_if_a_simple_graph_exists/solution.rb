# LeetCode 3656 - Determine if a Simple Graph Exists
# https://leetcode.com/problems/determine-if-a-simple-graph-exists/

# @param {Integer[]} degrees
# @return {Boolean}
def simple_graph_exists(degrees)
  n = degrees.length
  d = degrees.sort.reverse
  total = 0
  d.each do |x|
    return false if x < 0 || x >= n

    total += x
  end
  return false if total.odd?

  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + d[i] }
  (1..n).each do |k|
    right = 0
    (k...n).each { |i| right += d[i] < k ? d[i] : k }
    return false if prefix[k] > k * (k - 1) + right
  end
  true
end
