# LeetCode 3864 - Minimum Cost to Partition a Binary String
# https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

# @param {String} s
# @param {Integer} enc_cost
# @param {Integer} flat_cost
# @return {Integer}
def min_cost(s, enc_cost, flat_cost)
  n = s.length
  pre = Array.new(n + 1, 0)
  (1..n).each { |i| pre[i] = pre[i - 1] + (s[i - 1].ord - 48) }
  dfs = nil
  dfs = lambda do |l, r|
    x = pre[r] - pre[l]
    res = x != 0 ? (r - l) * x * enc_cost : flat_cost
    if (r - l).even?
      m = (l + r) / 2
      res = [res, dfs.call(l, m) + dfs.call(m, r)].min
    end
    res
  end
  dfs.call(0, n)
end
