# LeetCode 1160 - Find Words That Can Be Formed by Characters
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

# @param {String[]} words
# @param {String} chars
# @return {Integer}
def count_characters(words, chars)
  avail = Hash.new(0)
  chars.each_char { |c| avail[c] += 1 }
  ans = 0
  words.each do |word|
    need = Hash.new(0)
    word.each_char { |c| need[c] += 1 }
    ok = need.all? { |c, v| v <= avail[c] }
    ans += word.length if ok
  end
  ans
end
