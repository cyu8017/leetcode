# LeetCode 3003 - Maximize the Number of Partitions After Operations
# https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def max_partitions_after_operations(s, k)
  n = s.length
  memo = {}
  popcount = lambda do |x|
    c = 0
    while x != 0
      c += x & 1
      x >>= 1
    end
    c
  end
  dfs = lambda do |i, cur, t|
    return 1 if i >= n

    kkey = (i << 32) | (cur << 1) | t
    return memo[kkey] if memo.key?(kkey)

    v = 1 << (s[i].ord - 97)
    nxt = cur | v
    ans = if popcount.call(nxt) > k
            dfs.call(i + 1, v, t) + 1
          else
            dfs.call(i + 1, nxt, t)
          end
    if t > 0
      26.times do |j|
        nxt2 = cur | (1 << j)
        ans = if popcount.call(nxt2) > k
                [ans, dfs.call(i + 1, 1 << j, 0) + 1].max
              else
                [ans, dfs.call(i + 1, nxt2, 0)].max
              end
      end
    end
    memo[kkey] = ans
    ans
  end
  dfs.call(0, 0, 1)
end
