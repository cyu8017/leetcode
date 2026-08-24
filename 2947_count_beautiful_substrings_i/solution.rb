# LeetCode 2947 - Count Beautiful Substrings I
# https://leetcode.com/problems/count-beautiful-substrings-i/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def beautiful_substrings(s, k)
  ans = 0
  n = s.length
  n.times do |i|
    v = 0
    c = 0
    i.upto(n - 1) do |j|
      if vowel?(s[j])
        v += 1
      else
        c += 1
      end
      ans += 1 if v == c && (v * c) % k == 0
    end
  end
  ans
end

def vowel?(ch)
  ch == "a" || ch == "e" || ch == "i" || ch == "o" || ch == "u"
end
