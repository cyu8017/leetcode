# LeetCode 0953 - Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/

# @param {String[]} words
# @param {String} order
# @return {Boolean}
def is_alien_sorted(words, order)
  rank = {}
  order.each_char.with_index { |c, i| rank[c] = i }
  key = ->(w) { w.chars.map { |c| rank[c] } }
  (0...(words.length - 1)).all? { |i| (key.call(words[i]) <=> key.call(words[i + 1])) <= 0 }
end
