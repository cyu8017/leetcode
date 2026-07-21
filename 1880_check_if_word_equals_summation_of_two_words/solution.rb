# LeetCode 1880 - Check if Word Equals Summation of Two Words
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

# @param {String} first_word
# @param {String} second_word
# @param {String} target_word
# @return {Boolean}
def is_sum_equal(first_word, second_word, target_word)
  value = lambda { |word| word.chars.map { |ch| (ch.ord - "a".ord).to_s }.join.to_i }
  value.call(first_word) + value.call(second_word) == value.call(target_word)
end
