# LeetCode 3887 - Incremental Even-Weighted Cycle Queries
# https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_valid_edges(n, edges)
  parent = (0...n).to_a
  size = Array.new(n, 1)
  parity = Array.new(n, 0)
  find = nil
  find = lambda do |x|
    return [x, 0] if parent[x] == x
    root, p = find.call(parent[x])
    parity[x] ^= p
    parent[x] = root
    [root, parity[x]]
  end
  ans = 0
  edges.each do |e|
    ru, pu = find.call(e[0])
    rv, pv = find.call(e[1])
    if ru == rv
      ans += 1 if (pu ^ pv) == e[2]
      next
    end
    if size[ru] < size[rv]
      ru, rv = rv, ru
      pu, pv = pv, pu
    end
    parent[rv] = ru
    parity[rv] = pu ^ pv ^ e[2]
    size[ru] += size[rv]
    ans += 1
  end
  ans
end
