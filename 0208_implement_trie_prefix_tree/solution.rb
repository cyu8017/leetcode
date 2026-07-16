# LeetCode 0208 - Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode
  attr_accessor :children, :is_word

  def initialize
    @children = {}
    @is_word = false
  end
end

class Trie
  def initialize
    @root = TrieNode.new
  end

  def insert(word)
    node = @root
    word.each_char do |char|
      node.children[char] ||= TrieNode.new
      node = node.children[char]
    end
    node.is_word = true
  end

  def search(word)
    node = find(word)
    !node.nil? && node.is_word
  end

  def starts_with(prefix)
    !find(prefix).nil?
  end

  private

  def find(text)
    node = @root
    text.each_char do |char|
      return nil unless node.children.key?(char)

      node = node.children[char]
    end
    node
  end
end