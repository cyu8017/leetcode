# LeetCode 0890 - Find and Replace Pattern
# https://leetcode.com/problems/find-and-replace-pattern/

# @param {String[]} words
# @param {String} pattern
# @return {String[]}
def find_and_replace_pattern(words, pattern)
  normalize = lambda do |s|
    mapping = {}
    s.chars.map do |ch|
      mapping[ch] = mapping.length unless mapping.key?(ch)
      mapping[ch]
    end
  end
  target = normalize.call(pattern)
  words.select { |w| normalize.call(w) == target }
end
