# LeetCode 0876 - Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

# @param {ListNode} head
# @return {ListNode}
def middle_node(head)
  slow = head
  fast = head
  while fast && fast.next
    slow = slow.next
    fast = fast.next.next
  end
  slow
end
