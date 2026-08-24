# LeetCode 2487 - Remove Nodes From Linked List
# https://leetcode.com/problems/remove-nodes-from-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

# @param {ListNode} head
# @return {ListNode}
def remove_nodes(head)
  rev = lambda do |node|
    prev = nil
    while node
      nxt = node.next
      node.next = prev
      prev = node
      node = nxt
    end
    prev
  end

  head = rev.call(head)
  mx = 0
  dummy = ListNode.new(0, head)
  prev = dummy
  while prev.next
    if prev.next.val >= mx
      mx = prev.next.val
      prev = prev.next
    else
      prev.next = prev.next.next
    end
  end
  rev.call(dummy.next)
end
