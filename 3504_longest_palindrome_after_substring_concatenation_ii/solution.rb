# LeetCode 3504 - Longest Palindrome After Substring Concatenation II
# https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/

# @param {String} s
# @param {String} t
# @return {Integer}
def longest_palindrome(s, t)
  expand = lambda do |str, g, l, r|
    while l >= 0 && r < str.length && str[l] == str[r]
      g[l] = [g[l], r - l + 1].max
      l -= 1
      r += 1
    end
  end
  calc = lambda do |str|
    n = str.length
    g = Array.new(n, 0)
    (0...n).each do |i|
      expand.call(str, g, i, i)
      expand.call(str, g, i, i + 1)
    end
    g
  end
  m = s.length
  n = t.length
  t = t.reverse
  g1 = calc.call(s)
  g2 = calc.call(t)
  ans = 0
  g1.each { |v| ans = [ans, v].max }
  g2.each { |v| ans = [ans, v].max }
  f = Array.new(m + 1) { Array.new(n + 1, 0) }
  (1..m).each do |i|
    (1..n).each do |j|
      next unless s[i - 1] == t[j - 1]
      f[i][j] = f[i - 1][j - 1] + 1
      a = i < m ? g1[i] : 0
      b = j < n ? g2[j] : 0
      ans = [ans, f[i][j] * 2 + a].max
      ans = [ans, f[i][j] * 2 + b].max
    end
  end
  ans
end
