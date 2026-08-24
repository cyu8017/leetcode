# LeetCode 2047 - Number of Valid Words in a Sentence
# https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

# @param {String} sentence
# @return {Integer}
def count_valid_words(sentence)
  valid = lambda do |w|
    return false if w.empty?

    hyphen = 0
    w.each_char.with_index do |c, i|
      return false if c >= "0" && c <= "9"

      if c == "-"
        hyphen += 1
        return false if hyphen > 1 || i.zero? || i == w.length - 1
        return false unless w[i - 1] >= "a" && w[i - 1] <= "z" && w[i + 1] >= "a" && w[i + 1] <= "z"
      elsif "!.,".include?(c)
        return false if i != w.length - 1
      else
        return false unless c >= "a" && c <= "z"
      end
    end
    true
  end
  sentence.split(" ").count { |tok| valid.call(tok) }
end
