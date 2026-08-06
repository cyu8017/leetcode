# LeetCode 1156 - Swap For Longest Repeated Character Substring
# https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

# @param {String} text
# @return {Integer}
def max_rep_opt1(text)
  count = Hash.new(0)
  text.each_char { |ch| count[ch] += 1 }
  n = text.length
  ans = 0
  i = 0
  while i < n
    j = i
    j += 1 while j < n && text[j] == text[i]
    length = j - i
    k = j + 1
    k += 1 while k < n && text[k] == text[i]
    length2 = j < n ? k - j - 1 : 0
    ans = [ans, [length + length2 + 1, count[text[i]]].min].max
    i = j
  end
  ans
end
