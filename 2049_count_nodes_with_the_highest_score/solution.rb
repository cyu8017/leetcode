# LeetCode 2049 - Count Nodes With the Highest Score
# https://leetcode.com/problems/count-nodes-with-the-highest-score/

# @param {Integer[]} parents
# @return {Integer}
def count_highest_score_nodes(parents)
  n = parents.length
  children = Array.new(n) { [] }
  (1...n).each { |i| children[parents[i]] << i }
  size = Array.new(n, 0)
  dfs = lambda do |u|
    size[u] = 1
    children[u].each { |v| size[u] += dfs.call(v) }
    size[u]
  end
  dfs.call(0)
  best = 0
  ans = 0
  n.times do |u|
    score = 1
    children[u].each { |v| score *= size[v] }
    up = n - size[u]
    score *= up if up > 0
    if score > best
      best = score
      ans = 1
    elsif score == best
      ans += 1
    end
  end
  ans
end
