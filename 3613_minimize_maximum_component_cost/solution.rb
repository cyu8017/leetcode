# LeetCode 3613 - Minimize Maximum Component Cost
# https://leetcode.com/problems/minimize-maximum-component-cost/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} k
# @return {Integer}
def min_cost(n, edges, k)
  p = (0...n).to_a
  find = nil
  find = lambda do |x|
    p[x] = find.call(p[x]) if p[x] != x
    p[x]
  end
  return 0 if k == n

  edges = edges.sort_by { |e| e[2] }
  cnt = n
  edges.each do |e|
    pu = find.call(e[0])
    pv = find.call(e[1])
    if pu != pv
      p[pu] = pv
      cnt -= 1
      return e[2] if cnt <= k
    end
  end
  0
end
