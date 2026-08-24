# LeetCode 2484 - Count Palindromic Subsequences
# https://leetcode.com/problems/count-palindromic-subsequences/

# @param {String} s
# @return {Integer}
def count_palindromes(s)
  mod = 1_000_000_007
  n = s.length
  pref = Array.new(n) { Array.new(10) { Array.new(10, 0) } }
  suf = Array.new(n) { Array.new(10) { Array.new(10, 0) } }
  cnt = Array.new(10, 0)
  (0...n).each do |i|
    if i > 0
      (0...10).each do |a|
        (0...10).each { |b| pref[i][a][b] = pref[i - 1][a][b] }
      end
    end
    d = s[i].ord - 48
    (0...10).each { |a| pref[i][a][d] += cnt[a] }
    cnt[d] += 1
  end
  cnt = Array.new(10, 0)
  (n - 1).downto(0) do |i|
    if i + 1 < n
      (0...10).each do |a|
        (0...10).each { |b| suf[i][a][b] = suf[i + 1][a][b] }
      end
    end
    d = s[i].ord - 48
    (0...10).each { |a| suf[i][a][d] += cnt[a] }
    cnt[d] += 1
  end
  ans = 0
  (2...(n - 2)).each do |i|
    (0...10).each do |a|
      (0...10).each { |b| ans = (ans + pref[i - 1][a][b] * suf[i + 1][a][b]) % mod }
    end
  end
  ans
end
