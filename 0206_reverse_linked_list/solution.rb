# LeetCode 0206 - Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

# @param {ListNode} head
# @return {ListNode}
def reverse_list(head)
  previous = nil
  current = head
  while current
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node
  end
  previous
end