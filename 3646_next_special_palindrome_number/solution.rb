# LeetCode 3646 - Next Special Palindrome Number
# https://leetcode.com/problems/next-special-palindrome-number/

# @param {Integer} n
# @return {Integer}
def special_palindrome(n)
  cands = []
  half_cnt = Array.new(10, 0)
  mid = 0
  half_len = 0
  dfs = nil
  dfs = lambda do |pos, cur|
    if pos == half_len
      left = cur.join
      s = left
      s += mid.to_s if mid > 0
      s += left.reverse
      cands << s.to_i
      return
    end
    (1..9).each do |d|
      next if half_cnt[d] == 0

      half_cnt[d] -= 1
      cur << d
      dfs.call(pos + 1, cur)
      cur.pop
      half_cnt[d] += 1
    end
  end
  gen = lambda do |mask|
    total = 0
    odd = 0
    (1..9).each do |d|
      next unless (mask >> d) & 1 == 1

      total += d
      odd += 1 if d.odd?
    end
    return if total == 0 || total > 18 || odd > 1

    10.times { |i| half_cnt[i] = 0 }
    mid = 0
    (1..9).each do |d|
      next if ((mask >> d) & 1) == 0

      half_cnt[d] = d / 2
      mid = d if d.odd?
    end
    half_len = total / 2
    dfs.call(0, [])
  end
  (1...(1 << 10)).each do |mask|
    next if mask & 1 != 0

    gen.call(mask)
  end
  cands.sort!
  cands.each { |v| return v if v > n }
  -1
end
