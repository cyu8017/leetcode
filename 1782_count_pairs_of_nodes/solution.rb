# LeetCode 1782 - Count Pairs Of Nodes
# https://leetcode.com/problems/count-pairs-of-nodes/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} queries
# @return {Integer[]}
def count_pairs(n, edges, queries)
  deg = Array.new(n + 1, 0)
  shared = Hash.new(0)
  edges.each do |edge|
    a, b = edge
    a, b = b, a if a > b
    deg[a] += 1
    deg[b] += 1
    shared[[a, b]] += 1
  end
  sorted_deg = deg[1..].sort
  queries.map do |q|
    res = 0
    left = 0
    right = n - 1
    while left < right
      if sorted_deg[left] + sorted_deg[right] > q
        res += right - left
        right -= 1
      else
        left += 1
      end
    end
    shared.each do |(a, b), count|
      sum = deg[a] + deg[b]
      res -= 1 if sum > q && q >= sum - count
    end
    res
  end
end
