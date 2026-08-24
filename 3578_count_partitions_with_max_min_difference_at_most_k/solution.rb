# LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_partitions(nums, k)
  mod = 1000000007
  sl = {}
  n = nums.length
  f = Array.new(n + 1, 0)
  g = Array.new(n + 1, 0)
  f[0] = g[0] = 1
  keys = []
  add = lambda do |v|
    unless sl.key?(v)
      sl[v] = 0
      lo = 0
      hi = keys.length
      while lo < hi
        mid = (lo + hi) >> 1
        if keys[mid] < v
          lo = mid + 1
        else
          hi = mid
        end
      end
      keys.insert(lo, v)
    end
    sl[v] += 1
  end
  rem = lambda do |v|
    c = sl[v] - 1
    if c == 0
      sl.delete(v)
      ix = keys.index(v)
      keys.delete_at(ix) if ix
    else
      sl[v] = c
    end
  end
  l = 1
  (1..n).each do |r|
    add.call(nums[r - 1])
    while keys[-1] - keys[0] > k
      rem.call(nums[l - 1])
      l += 1
    end
    f[r] = g[r - 1]
    f[r] = (f[r] - g[l - 2] + mod) % mod if l >= 2
    g[r] = (g[r - 1] + f[r]) % mod
  end
  f[n]
end
