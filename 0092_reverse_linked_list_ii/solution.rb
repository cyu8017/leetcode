# LeetCode 0092 - Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @param {Integer} left
# @param {Integer} right
# @return {ListNode}
def reverse_between(head, left, right)
  return head if head.nil? || left == right

  dummy = ListNode.new(0, head)
  before = dummy
  (left - 1).times { before = before.next }

  start = before.next
  current = start.next

  (right - left).times do
    start.next = current.next
    current.next = before.next
    before.next = current
    current = start.next
  end

  dummy.next
end
