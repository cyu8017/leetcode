# LeetCode 3544 - Subtree Inversion Sum
# https://leetcode.com/problems/subtree-inversion-sum/

# @param {Integer[][]} edges
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subtree_inversion_sum(edges, nums, k)
  n = edges.length + 1
  graph = Array.new(n) { [] }
  edges.each do |e|
    graph[e[0]] << e[1]
    graph[e[1]] << e[0]
  end
  parent = Array.new(n, -1)
  memo = {}
  dp = nil
  dp = lambda do |u, steps, inv|
    key = [u, steps, inv]
    return memo[key] if memo.key?(key)
    num = nums[u]
    num = -num if inv
    neg_num = -num
    graph[u].each do |v|
      next if v == parent[u]
      parent[v] = u
      ns = steps + 1
      ns = k if ns > k
      num += dp.call(v, ns, inv)
      neg_num += dp.call(v, 1, !inv) if steps == k
    end
    res = num
    res = neg_num if steps == k && neg_num > res
    memo[key] = res
    res
  end
  dp.call(0, k, false)
end
