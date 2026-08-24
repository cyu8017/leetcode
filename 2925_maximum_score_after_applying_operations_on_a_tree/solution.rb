# LeetCode 2925 - Maximum Score After Applying Operations on a Tree
# https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

# @param {Integer[][]} edges
# @param {Integer[]} values
# @return {Integer}
def maximum_score_after_operations(edges, values)
  n = values.length
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  total = values.sum

  dfs = lambda do |u, p|
    sum_kids = 0
    is_leaf = true
    g[u].each do |v|
      next if v == p

      is_leaf = false
      sum_kids += dfs.call(v, u)
    end
    return values[u] if is_leaf

    values[u] < sum_kids ? values[u] : sum_kids
  end

  total - dfs.call(0, -1)
end
