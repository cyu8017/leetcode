# LeetCode 0024 - Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next = nil)
    @val = val
    @next = next
  end
end

# @param {ListNode} head
# @return {ListNode}
def swap_pairs(head)
  dummy = ListNode.new(0, head)
  previous = dummy

  while previous.next && previous.next.next
    first = previous.next
    second = previous.next.next
    first.next = second.next
    second.next = first
    previous.next = second
    previous = first
  end

  dummy.next
end
