# LeetCode 0019 - Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next = nil)
    @val = val
    @next = next
  end
end

# @param {ListNode} head
# @param {Integer} n
# @return {ListNode}
def remove_nth_from_end(head, n)
  dummy = ListNode.new(0, head)
  fast = dummy
  slow = dummy

  n.times { fast = fast.next }

  while fast.next
    fast = fast.next
    slow = slow.next
  end

  slow.next = slow.next.next
  dummy.next
end
