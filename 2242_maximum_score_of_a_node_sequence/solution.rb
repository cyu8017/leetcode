# LeetCode 2242 - Maximum Score of a Node Sequence
# https://leetcode.com/problems/maximum-score-of-a-node-sequence/

# @param {Integer[]} scores
# @param {Integer[][]} edges
# @return {Integer}
def maximum_score(scores, edges)
  n = scores.length
  top = Array.new(n) { [] }
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  n.times do |i|
    g[i].each do |v|
      top[i] << v
      j = top[i].length - 1
      while j > 0
        if scores[top[i][j]] > scores[top[i][j - 1]]
          top[i][j], top[i][j - 1] = top[i][j - 1], top[i][j]
        end
        j -= 1
      end
      top[i] = top[i][0, 3] if top[i].length > 3
    end
  end
  ans = -1
  edges.each do |a, b|
    top[a].each do |c|
      next if c == b

      top[b].each do |d|
        next if d == a || d == c

        ans = [ans, scores[a] + scores[b] + scores[c] + scores[d]].max
      end
    end
  end
  ans
end
