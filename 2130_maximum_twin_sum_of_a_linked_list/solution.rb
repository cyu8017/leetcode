# LeetCode 2130 - Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {Integer}
def pair_sum(head)
  slow = head
  fast = head
  while fast && fast.next
    slow = slow.next
    fast = fast.next.next
  end
  prev = nil
  while slow
    nxt = slow.next
    slow.next = prev
    prev = slow
    slow = nxt
  end
  ans = 0
  a = head
  b = prev
  while b
    ans = [ans, a.val + b.val].max
    a = a.next
    b = b.next
  end
  ans
end
