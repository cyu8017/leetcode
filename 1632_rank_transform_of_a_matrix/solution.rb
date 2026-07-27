# LeetCode 1632 - Rank Transform of a Matrix
# https://leetcode.com/problems/rank-transform-of-a-matrix/

# @param {Integer[][]} matrix
# @return {Integer[][]}
def matrix_rank_transform(matrix)
  m = matrix.length
  n = matrix[0].length
  groups = Hash.new { |h, k| h[k] = [] }
  m.times do |i|
    n.times { |j| groups[matrix[i][j]] << [i, j] }
  end
  rank = Array.new(m + n, 0)
  ans = Array.new(m) { Array.new(n, 0) }
  groups.keys.sort.each do |value|
    parent = {}
    find = lambda do |x|
      parent[x] = x unless parent.key?(x)
      parent[x] = find.call(parent[x]) if parent[x] != x
      parent[x]
    end
    groups[value].each do |i, j|
      a = find.call(i)
      b = find.call(m + j)
      parent[a] = b
    end
    best = Hash.new(0)
    groups[value].each do |i, j|
      root = find.call(i)
      best[root] = [best[root], rank[i], rank[m + j]].max
    end
    groups[value].each do |i, j|
      r = best[find.call(i)] + 1
      ans[i][j] = r
    end
    groups[value].each do |i, j|
      rank[i] = [rank[i], ans[i][j]].max
      rank[m + j] = [rank[m + j], ans[i][j]].max
    end
  end
  ans
end
