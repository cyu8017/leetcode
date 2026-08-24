# LeetCode 2095 - Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {ListNode}
def delete_middle(head)
  return nil if head.next.nil?

  slow = head
  fast = head
  prev = nil
  while fast && fast.next
    prev = slow
    slow = slow.next
    fast = fast.next.next
  end
  prev.next = slow.next
  head
end
