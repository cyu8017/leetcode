# LeetCode 0824 - Goat Latin
# https://leetcode.com/problems/goat-latin/

# @param {String} sentence
# @return {String}
def to_goat_latin(sentence)
  vowels = "aeiouAEIOU"
  sentence.split.each_with_index.map do |word, idx|
    goat = if vowels.include?(word[0])
             word + "ma"
           else
             word[1..] + word[0] + "ma"
           end
    goat + ("a" * (idx + 1))
  end.join(" ")
end
