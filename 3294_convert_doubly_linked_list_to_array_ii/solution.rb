# LeetCode 3294 - Convert Doubly Linked List to Array II
# https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

class Node
  attr_accessor :val, :prev, :next

  def initialize(val = 0, prev = nil, nxt = nil)
    @val = val
    @prev = prev
    @next = nxt
  end
end

# @param {Node} node
# @return {Integer[]}
def to_array(node)
  node = node.prev while !node.nil? && !node.prev.nil?
  ans = []
  until node.nil?
    ans << node.val
    node = node.next
  end
  ans
end
