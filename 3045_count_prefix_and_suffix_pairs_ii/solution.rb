# LeetCode 3045 - Count Prefix and Suffix Pairs II
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

class Node
  attr_accessor :children, :cnt

  def initialize
    @children = {}
    @cnt = 0
  end
end

# @param {String[]} words
# @return {Integer}
def count_prefix_suffix_pairs(words)
  trie = Node.new
  ans = 0
  words.each do |s|
    node = trie
    m = s.length
    m.times do |i|
      p = s[i].ord * 32 + s[m - i - 1].ord
      nxt = node.children[p]
      unless nxt
        nxt = Node.new
        node.children[p] = nxt
      end
      node = nxt
      ans += node.cnt
    end
    node.cnt += 1
  end
  ans
end
