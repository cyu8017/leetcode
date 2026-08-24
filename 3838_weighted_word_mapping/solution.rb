# LeetCode 3838 - Weighted Word Mapping
# https://leetcode.com/problems/weighted-word-mapping/

# @param {String[]} words
# @param {Integer[]} weights
# @return {String}
def map_word_weights(words, weights)
  ans = []
  words.each do |w|
    s = 0
    w.each_byte { |c| s = (s + weights[c - 97]) % 26 }
    ans << (97 + (25 - s)).chr
  end
  ans.join
end
