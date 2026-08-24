# LeetCode 3263 - Convert Doubly Linked List to Array I
# https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

class Node
  attr_accessor :val, :prev, :next
  def initialize(val = 0, prev = nil, nxt = nil)
    @val = val
    @prev = prev
    @next = nxt
  end
end

# @param {Node} head
# @return {Integer[]}
def to_array(head)
  ans = []
  while head
    ans << head.val
    head = head.next
  end
  ans
end
