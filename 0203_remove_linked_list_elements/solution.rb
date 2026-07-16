# LeetCode 0203 - Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

# @param {ListNode} head
# @param {Integer} val
# @return {ListNode}
def remove_elements(head, val)
  dummy = ListNode.new(0, head)
  current = dummy
  while current.next
    if current.next.val == val
      current.next = current.next.next
    else
      current = current.next
    end
  end
  dummy.next
end