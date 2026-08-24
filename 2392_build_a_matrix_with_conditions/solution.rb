# LeetCode 2392 - Build a Matrix With Conditions
# https://leetcode.com/problems/build-a-matrix-with-conditions/

# @param {Integer} k
# @param {Integer[][]} row_conditions
# @param {Integer[][]} col_conditions
# @return {Integer[][]}
def build_matrix(k, row_conditions, col_conditions)
  topo = lambda do |conds|
    g = Array.new(k + 1) { [] }
    indeg = Array.new(k + 1, 0)
    conds.each do |c|
      g[c[0]] << c[1]
      indeg[c[1]] += 1
    end
    q = k.downto(1).select { |i| indeg[i] == 0 }
    order = []
    until q.empty?
      u = q.shift
      order << u
      g[u].each do |v|
        indeg[v] -= 1
        q << v if indeg[v] == 0
      end
    end
    return nil if order.length != k
    order
  end
  row_order = topo.call(row_conditions)
  col_order = topo.call(col_conditions)
  return [] if row_order.nil? || col_order.nil?
  row_pos = Array.new(k + 1, 0)
  col_pos = Array.new(k + 1, 0)
  (0...k).each do |i|
    row_pos[row_order[i]] = i
    col_pos[col_order[i]] = i
  end
  ans = Array.new(k) { Array.new(k, 0) }
  (1..k).each { |v| ans[row_pos[v]][col_pos[v]] = v }
  ans
end
