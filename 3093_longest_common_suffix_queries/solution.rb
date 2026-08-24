# LeetCode 3093 - Longest Common Suffix Queries
# https://leetcode.com/problems/longest-common-suffix-queries/

class Trie
  attr_accessor :children, :length, :idx
  def initialize
    @children = Array.new(26)
    @length = 1 << 30
    @idx = 1 << 30
  end
end

# @param {String[]} words_container
# @param {String[]} words_query
# @return {Integer[]}
def string_indices(words_container, words_query)
  insert = lambda do |t, w, i|
    node = t
    if node.length > w.length
      node.length = w.length
      node.idx = i
    end
    (w.length - 1).downto(0) do |k|
      cid = w[k].ord - 97
      node.children[cid] ||= Trie.new
      node = node.children[cid]
      if node.length > w.length
        node.length = w.length
        node.idx = i
      end
    end
  end

  query = lambda do |t, w|
    node = t
    (w.length - 1).downto(0) do |k|
      cid = w[k].ord - 97
      break if node.children[cid].nil?
      node = node.children[cid]
    end
    node.idx
  end

  trie = Trie.new
  words_container.each_with_index { |w, i| insert.call(trie, w, i) }
  words_query.map { |w| query.call(trie, w) }
end
