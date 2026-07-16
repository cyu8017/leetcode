# LeetCode 0328 - Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

class Solution
  def oddEvenList(head)
    return head if head.nil? || head.next.nil?

    odd = head
    even = head.next
    even_head = even
    while even && even.next
      odd.next = even.next
      odd = odd.next
      even.next = odd.next
      even = even.next
    end
    odd.next = even_head
    head
  end
end
