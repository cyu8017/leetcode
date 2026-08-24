# LeetCode 0720 - Longest Word in Dictionary
# https://leetcode.com/problems/longest-word-in-dictionary/

# @param {String[]} words
# @return {String}
def longest_word(words)
  words = words.sort
  built = { "" => true }
  best = ""
  words.each do |word|
    if built[word[0...-1]]
      built[word] = true
      best = word if word.length > best.length
    end
  end
  best
end
