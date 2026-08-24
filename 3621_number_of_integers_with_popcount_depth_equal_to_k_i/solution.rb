# LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
# https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def popcount_depth(n, k)
  return n >= 1 ? 1 : 0 if k == 0

  bit_count = lambda do |x|
    c = 0
    while x > 0
      c += x & 1
      x >>= 1
    end
    c
  end

  depth = lambda do |x|
    return 100 if x <= 0

    d = 0
    while x > 1
      x = bit_count.call(x)
      d += 1
    end
    d
  end

  bits = []
  x = n
  while x > 0
    bits << (x & 1).to_s
    x /= 2
  end
  s = bits.empty? ? "0" : bits.reverse.join
  memo = {}
  dfs = nil
  dfs = lambda do |pos, tight, started, pc|
    if pos == s.length
      return 0 if started == 0
      return k == 1 ? 1 : 0 if pc == 1

      return depth.call(pc) == k - 1 ? 1 : 0
    end
    key = [pos, tight, started, pc]
    return memo[key] if memo.key?(key)

    up = tight == 1 ? s[pos].to_i : 1
    res = 0
    (0..up).each do |dig|
      nt = tight == 1 && dig == up ? 1 : 0
      res += if started == 0 && dig == 0
               dfs.call(pos + 1, nt, 0, 0)
             else
               dfs.call(pos + 1, nt, 1, pc + dig)
             end
    end
    memo[key] = res
    res
  end
  dfs.call(0, 1, 0, 0)
end
