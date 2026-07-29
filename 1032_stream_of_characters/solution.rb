# LeetCode 1032 - Stream of Characters
# https://leetcode.com/problems/stream-of-characters/

class StreamChecker
  def initialize(words)
    @trie = {}
    words.each do |word|
      node = @trie
      word.reverse.each_char do |ch|
        node[ch] ||= {}
        node = node[ch]
      end
      node["$"] = true
    end
    @stream = []
  end

  def query(letter)
    @stream << letter
    node = @trie
    @stream.reverse_each do |ch|
      return true if node["$"]
      return false unless node.key?(ch)

      node = node[ch]
    end
    !!node["$"]
  end
end
