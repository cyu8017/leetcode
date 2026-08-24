# LeetCode 0745 - Prefix and Suffix Search
# https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter
  def initialize(words)
    @lookup = {}
    words.each_with_index do |word, index|
      size = word.length
      (0..size).each do |i|
        (0..size).each do |j|
          @lookup[word[0...i] + "#" + word[j...]] = index
        end
      end
    end
  end

  def f(pref, suff)
    @lookup.fetch(pref + "#" + suff, -1)
  end
end
