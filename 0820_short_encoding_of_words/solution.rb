# LeetCode 0820 - Short Encoding of Words
# https://leetcode.com/problems/short-encoding-of-words/

# @param {String[]} words
# @return {Integer}
def minimum_length_encoding(words)
  good = words.each_with_object({}) { |w, h| h[w] = true }
  words.each do |word|
    (1...word.length).each { |i| good.delete(word[i..]) }
  end
  good.keys.sum { |word| word.length + 1 }
end
