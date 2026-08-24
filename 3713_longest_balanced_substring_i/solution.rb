# LeetCode 3713 - Longest Balanced Substring I
# https://leetcode.com/problems/longest-balanced-substring-i/

# @param {String} s
# @return {Integer}
def longest_balanced(s)
  n = s.length
  ans = 0
  (0...n).each do |i|
    cnt = Array.new(26, 0)
    mx = 0
    v = 0
    (i...n).each do |j|
      c = s[j].ord - 97
      cnt[c] += 1
      v += 1 if cnt[c] == 1
      mx = cnt[c] if cnt[c] > mx
      ans = j - i + 1 if mx * v == j - i + 1 && j - i + 1 > ans
    end
  end
  ans
end
