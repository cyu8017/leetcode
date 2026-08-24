# LeetCode 3517 - Smallest Palindromic Rearrangement I
# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

# @param {String} s
# @return {String}
def smallest_palindrome(s)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  t = ""
  ch = ""
  (0...26).each do |i|
    c = (97 + i).chr
    v = cnt[i] / 2
    t += c * v
    cnt[i] -= v * 2
    ch = c if cnt[i] == 1
  end
  sb = t
  sb += ch unless ch.empty?
  (t.length - 1).downto(0) { |i| sb += t[i] }
  sb
end
