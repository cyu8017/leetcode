# LeetCode 3715 - Sum of Perfect Square Ancestors
# https://leetcode.com/problems/sum-of-perfect-square-ancestors/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} nums
# @return {Integer}
def sum_of_ancestors(n, edges, nums)
  graph = Array.new(n) { [] }
  edges.each do |u, v|
    graph[u] << v
    graph[v] << u
  end
  kernel = lambda do |x|
    res = 1
    p = 2
    while p * p <= x
      cnt = 0
      while x % p == 0
        x /= p
        cnt += 1
      end
      res *= p if cnt.odd?
      p += 1
    end
    res *= x if x > 1
    res
  end
  ks = (0...n).map { |i| kernel.call(nums[i]) }
  freq = Hash.new(0)
  ans = 0
  dfs = nil
  dfs = lambda do |u, p|
    ans += freq[ks[u]]
    freq[ks[u]] += 1
    graph[u].each { |v| dfs.call(v, u) if v != p }
    freq[ks[u]] -= 1
  end
  dfs.call(0, -1)
  ans
end
