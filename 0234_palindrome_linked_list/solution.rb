# LeetCode 0234 - Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

# @param {ListNode} head
# @return {Boolean}
def is_palindrome(head)
  return true if head.nil? || head.next.nil?

  slow = head
  fast = head
  while fast&.next
    slow = slow.next
    fast = fast.next.next
  end

  prev = nil
  current = slow
  while current
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
  end

  left = head
  right = prev
  while right
    return false if left.val != right.val

    left = left.next
    right = right.next
  end
  true
end
