# LeetCode 1392 - Longest Happy Prefix
# https://leetcode.com/problems/longest-happy-prefix/

def longest_prefix(s)
  return '' if s.empty?
  pi = Array.new(s.length, 0)
  (1...s.length).each do |i|
    j = pi[i - 1]
    j = pi[j - 1] while j > 0 && s[i] != s[j]
    j += 1 if s[i] == s[j]
    pi[i] = j
  end
  s[0, pi[-1]]
end
