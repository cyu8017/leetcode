# LeetCode 0082 - Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {ListNode}
def delete_duplicates(head)
  dummy = ListNode.new(0, head)
  previous = dummy

  while head
    if head.next && head.val == head.next.val
      while head.next && head.val == head.next.val
        head = head.next
      end
      previous.next = head.next
    else
      previous = previous.next
    end
    head = head.next
  end

  dummy.next
end
