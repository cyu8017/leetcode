# LeetCode 3032 - Count Numbers With Unique Digits II
# https://leetcode.com/problems/count-numbers-with-unique-digits-ii/

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def number_count(a, b)
  count_unique(b) - count_unique(a - 1)
end

def count_unique(n)
  return 0 if n < 0

  num = n.to_s
  f = Array.new(num.length) { Array.new(1 << 10, -1) }
  dfs = lambda do |pos, mask, limit|
    return mask != 0 ? 1 : 0 if pos >= num.length
    return f[pos][mask] if !limit && f[pos][mask] != -1

    up = limit ? (num[pos].ord - 48) : 9
    ans = 0
    (0..up).each do |i|
      next if ((mask >> i) & 1) != 0

      nxt = mask | (1 << i)
      nxt = 0 if mask == 0 && i == 0
      ans += dfs.call(pos + 1, nxt, limit && i == up)
    end
    f[pos][mask] = ans unless limit
    ans
  end
  dfs.call(0, 0, true)
end

def solve(*args)
  number_count(*args)
end
