# LeetCode 0648 - Replace Words
# https://leetcode.com/problems/replace-words/

# @param {String[]} dictionary
# @param {String} sentence
# @return {String}
def replace_words(dictionary, sentence)
  roots = dictionary.to_h { |word| [word, true] }

  replace = lambda do |word|
    (1..word.length).each do |i|
      prefix = word[0, i]
      return prefix if roots.key?(prefix)
    end
    word
  end

  sentence.split.map { |word| replace.call(word) }.join(" ")
end
