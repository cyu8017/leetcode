# LeetCode 0804 - Unique Morse Code Words
# https://leetcode.com/problems/unique-morse-code-words/

# @param {String[]} words
# @return {Integer}
def unique_morse_representations(words)
  codes = %w[
    .- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. ---
    .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..
  ]
  words.map { |word| word.chars.map { |ch| codes[ch.ord - 97] }.join }.uniq.length
end
