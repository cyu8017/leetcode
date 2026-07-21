# LeetCode 1804 - Implement Trie II (Prefix Tree)
# https://leetcode.com/problems/implement-trie-ii-prefix-tree/

class Trie
  def initialize
    @root = { children: {}, word_count: 0, prefix_count: 0 }
  end

  # @param {String} word
  # @return {Void}
  def insert(word)
    node = @root
    word.each_char do |ch|
      node[:children][ch] ||= { children: {}, word_count: 0, prefix_count: 0 }
      node = node[:children][ch]
      node[:prefix_count] += 1
    end
    node[:word_count] += 1
    nil
  end

  # @param {String} word
  # @return {Integer}
  def countWordsEqualTo(word)
    node = find(word)
    node ? node[:word_count] : 0
  end

  # @param {String} prefix
  # @return {Integer}
  def countWordsStartingWith(prefix)
    node = find(prefix)
    node ? node[:prefix_count] : 0
  end

  # @param {String} word
  # @return {Void}
  def erase(word)
    node = @root
    word.each_char do |ch|
      node = node[:children][ch]
      node[:prefix_count] -= 1
    end
    node[:word_count] -= 1
    nil
  end

  private

  def find(text)
    node = @root
    text.each_char do |ch|
      return nil unless node[:children].key?(ch)
      node = node[:children][ch]
    end
    node
  end
end
