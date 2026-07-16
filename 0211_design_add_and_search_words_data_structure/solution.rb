# LeetCode 0211 - Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode
  attr_accessor :children, :is_word

  def initialize
    @children = {}
    @is_word = false
  end
end

class WordDictionary
  def initialize
    @root = TrieNode.new
  end

  def add_word(word)
    node = @root
    word.each_char do |char|
      node.children[char] ||= TrieNode.new
      node = node.children[char]
    end
    node.is_word = true
  end

  def search(word)
    dfs(@root, word, 0)
  end

  private

  def dfs(node, word, index)
    return node.is_word if index == word.length

    char = word[index]
    if char == "."
      node.children.values.each do |child|
        return true if dfs(child, word, index + 1)
      end
      return false
    end

    return false unless node.children.key?(char)

    dfs(node.children[char], word, index + 1)
  end
end
