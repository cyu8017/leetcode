# LeetCode 0061 - Rotate List
# https://leetcode.com/problems/rotate-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @param {Integer} k
# @return {ListNode}
def rotate_right(head, k)
  return head if head.nil? || head.next.nil?

  tail = head
  length = 1
  while tail.next
    tail = tail.next
    length += 1
  end

  tail.next = head
  k %= length
  if k.zero?
    tail.next = nil
    return head
  end

  steps = length - k
  new_tail = head
  (steps - 1).times { new_tail = new_tail.next }

  new_head = new_tail.next
  new_tail.next = nil
  new_head
end
