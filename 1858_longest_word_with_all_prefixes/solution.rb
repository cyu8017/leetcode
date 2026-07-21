# LeetCode 1858 - Longest Word With All Prefixes
# https://leetcode.com/problems/longest-word-with-all-prefixes/

require "set"

# @param {String[]} words
# @return {String}
def longest_word(words)
  word_set = words.to_set
  best = ""

  words.each do |word|
    prefix = word
    valid = true
    while !prefix.empty?
      unless word_set.include?(prefix)
        valid = false
        break
      end
      prefix = prefix[0...-1]
    end

    if valid && (word.length > best.length || (word.length == best.length && word < best))
      best = word
    end
  end

  best
end
