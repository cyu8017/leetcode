# LeetCode 2999 - Count the Number of Powerful Integers
# https://leetcode.com/problems/count-the-number-of-powerful-integers/

# @param {Integer} start
# @param {Integer} finish
# @param {Integer} limit
# @param {String} s
# @return {Integer}
def number_of_powerful_int(start, finish, limit, s)
  count_powerful(finish, limit, s) - count_powerful(start - 1, limit, s)
end

def count_powerful(num, limit, s)
  return 0 if num < 0

  s.length.times { |i| return 0 if s[i].ord - 48 > limit }
  t = num.to_s
  n = t.length
  sn = s.length
  return 0 if n < sn

  ans = 0
  (sn...n).each do |length|
    pre_len = length - sn
    if pre_len == 0
      ans += 1
    else
      ways = limit
      (1...pre_len).each { |_| ways *= limit + 1 }
      ans += ways
    end
  end
  pref = n - sn
  memo = {}
  dfs = lambda do |i, tight|
    if i == pref
      return tight ? (t[pref..-1] >= s ? 1 : 0) : 1
    end

    key = (i << 1) | (tight ? 1 : 0)
    return memo[key] if memo.key?(key)

    up = tight ? (t[i].ord - 48) : limit
    up = limit if up > limit
    res = 0
    (0..up).each do |d|
      next if i == 0 && d == 0

      res += dfs.call(i + 1, tight && d == t[i].ord - 48)
    end
    memo[key] = res
    res
  end
  ans + dfs.call(0, true)
end
