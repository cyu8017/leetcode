# LeetCode 1397 - Find All Good Strings
# https://leetcode.com/problems/find-all-good-strings/

def find_good_strings(n, s1, s2, evil)
  mod = 1_000_000_007
  m = evil.length
  pi = Array.new(m, 0)
  (1...m).each do |i|
    j = pi[i - 1]
    j = pi[j - 1] while j > 0 && evil[i] != evil[j]
    j += 1 if evil[i] == evil[j]
    pi[i] = j
  end
  trans = Array.new(m) { Array.new(26, 0) }
  m.times do |j|
    26.times do |x|
      c = (97 + x).chr
      k = j
      k = pi[k - 1] while k > 0 && evil[k] != c
      k += 1 if evil[k] == c
      trans[j][x] = k
    end
  end
  memo = {}
  dp = lambda do |i, j, lo, hi|
    key = [i, j, lo, hi]
    return memo[key] if memo.key?(key)
    return 0 if j == m
    return 1 if i == n
    a = lo ? s1[i].ord - 97 : 0
    b = hi ? s2[i].ord - 97 : 25
    ans = 0
    (a..b).each do |x|
      ans += dp.call(i + 1, trans[j][x], lo && x == a, hi && x == b)
    end
    memo[key] = ans % mod
  end
  dp.call(0, 0, true, true)
end
