# LeetCode 3330 - Find the Original Typed String I
# https://leetcode.com/problems/find-the-original-typed-string-i/

# @param {String} word
# @return {Integer}
def possible_string_count(word)
  ans = 1
  (1...word.length).each { |i| ans += 1 if word[i] == word[i - 1] }
  ans
end
