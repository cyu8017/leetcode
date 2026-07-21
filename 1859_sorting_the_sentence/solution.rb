# LeetCode 1859 - Sorting the Sentence
# https://leetcode.com/problems/sorting-the-sentence/

# @param {String} s
# @return {String}
def sort_sentence(s)
  tokens = s.split
  ordered = Array.new(tokens.length, "")
  tokens.each do |token|
    position = token[-1].to_i - 1
    ordered[position] = token[0...-1]
  end
  ordered.join(" ")
end
