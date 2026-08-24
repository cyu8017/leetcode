# LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
# https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

# @param {Integer[]} parent
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_non_adjacent_subsets(parent, nums, k)
  mod = 1_000_000_007
  n = parent.length
  children = Array.new(n) { [] }
  (1...n).each { |i| children[parent[i]] << i }
  dp0 = Array.new(n)
  dp1 = Array.new(n)
  (n - 1).downto(0) do |u|
    a = Array.new(k, 0)
    b = Array.new(k, 0)
    a[0] = 1
    b[(((nums[u] % k) + k) % k)] = 1
    children[u].each do |v|
      na = Array.new(k, 0)
      nb = Array.new(k, 0)
      k.times do |x|
        k.times do |y|
          all_child = (dp0[v][y] + dp1[v][y]) % mod
          na[(x + y) % k] = (na[(x + y) % k] + a[x] * all_child) % mod
          nb[(x + y) % k] = (nb[(x + y) % k] + b[x] * dp0[v][y]) % mod
        end
      end
      a = na
      b = nb
    end
    dp0[u] = a
    dp1[u] = b
  end
  ans = (dp0[0][0] + dp1[0][0] - 1) % mod
  ans += mod if ans < 0
  ans
end
