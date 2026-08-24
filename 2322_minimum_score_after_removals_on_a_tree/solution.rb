# LeetCode 2322 - Minimum Score After Removals on a Tree
# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

# @param {Integer[]} nums
# @param {Integer[][]} edges
# @return {Integer}
def minimum_score(nums, edges)
  n = nums.length
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  xorv = Array.new(n, 0)
  in_t = Array.new(n, 0)
  out_t = Array.new(n, 0)
  time = [0]
  dfs = lambda do |u, p|
    in_t[u] = time[0]
    time[0] += 1
    xorv[u] = nums[u]
    g[u].each do |v|
      if v != p
        dfs.call(v, u)
        xorv[u] ^= xorv[v]
      end
    end
    out_t[u] = time[0]
  end
  is_ancestor = lambda do |a, b|
    in_t[a] <= in_t[b] && out_t[b] <= out_t[a]
  end
  dfs.call(0, -1)
  total = xorv[0]
  ans = Float::INFINITY
  (1...n).each do |i|
    ((i + 1)...n).each do |j|
      if is_ancestor.call(i, j)
        a = xorv[j]
        b = xorv[i] ^ xorv[j]
        c = total ^ xorv[i]
      elsif is_ancestor.call(j, i)
        a = xorv[i]
        b = xorv[j] ^ xorv[i]
        c = total ^ xorv[j]
      else
        a = xorv[i]
        b = xorv[j]
        c = total ^ xorv[i] ^ xorv[j]
      end
      cand = [a, b, c].max - [a, b, c].min
      ans = cand if cand < ans
    end
  end
  ans.to_i
end
