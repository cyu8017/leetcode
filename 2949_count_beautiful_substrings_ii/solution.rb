# LeetCode 2949 - Count Beautiful Substrings II
# https://leetcode.com/problems/count-beautiful-substrings-ii/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def beautiful_substrings(s, k)
  x = 1
  x += 1 while (x * x) % k != 0
  freq = { [0, 0] => 1 }
  bal = 0
  vowels = 0
  ans = 0
  s.each_char do |ch|
    if vowel?(ch)
      bal += 1
      vowels += 1
    else
      bal -= 1
    end
    key = [bal, vowels % x]
    f = freq[key] || 0
    ans += f
    freq[key] = f + 1
  end
  ans
end

def vowel?(ch)
  ch == "a" || ch == "e" || ch == "i" || ch == "o" || ch == "u"
end
