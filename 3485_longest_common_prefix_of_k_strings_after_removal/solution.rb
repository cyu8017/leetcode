# LeetCode 3485 - Longest Common Prefix of K Strings After Removal
# https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

# @param {String[]} words
# @param {Integer} k
# @return {Integer[]}
def longest_common_prefix(words, k)
  n = words.length
  ans = Array.new(n, 0)
  (0...n).each do |i|
    rest = (0...n).select { |j| j != i }.map { |j| words[j] }
    if rest.length < k
      ans[i] = 0
      next
    end
    rest.sort!
    best = 0
    (0..(rest.length - k)).each do |j|
      best = [best, lcp_of_3485(rest[j, k])].max
    end
    ans[i] = best
  end
  ans
end

def lcp_of_3485(a)
  return 0 if a.empty?

  pref = a[0]
  (1...a.length).each do |t|
    s = a[t]
    i = 0
    i += 1 while i < pref.length && i < s.length && pref[i] == s[i]
    pref = pref[0...i]
    return 0 if pref.empty?
  end
  pref.length
end
