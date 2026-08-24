# LeetCode 0819 - Most Common Word
# https://leetcode.com/problems/most-common-word/

# @param {String} paragraph
# @param {String[]} banned
# @return {String}
def most_common_word(paragraph, banned)
  banned_set = banned.each_with_object({}) { |w, h| h[w] = true }
  words = paragraph.downcase.scan(/[a-z]+/).reject { |word| banned_set[word] }
  words.tally.max_by { |_, count| count }[0]
end
