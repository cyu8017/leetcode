# LeetCode 1721 - Swapping Nodes in a Linked List
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode
#   attr_accessor :val, :next
#   def initialize(val = 0, _next = nil)
#     @val = val
#     @next = _next
#   end
# end

# @param {ListNode} head
# @param {Integer} k
# @return {ListNode}
def swap_nodes(head, k)
  first = head
  (k - 1).times { first = first.next }
  fast = first
  second = head
  while fast.next
    fast = fast.next
    second = second.next
  end
  first.val, second.val = second.val, first.val
  head
end
