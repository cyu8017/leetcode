# LeetCode 1451 - Rearrange Words In A Sentence
# https://leetcode.com/problems/rearrange-words-in-a-sentence/

def arrange_words(text)
  words = text.downcase.split
  words.sort_by!(&:length)
  words.join(' ').sub(/\A./) { |c| c.upcase }
end
