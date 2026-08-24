# LeetCode 2816 - Double a Number Represented as a Linked List
# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {ListNode}
def double_it(head)
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
  carry = 0
  cur = head
  prev = nil
  while cur
    val = cur.val * 2 + carry
    cur.val = val % 10
    carry = val / 10
    prev = cur
    cur = cur.next
  end
  prev.next = ListNode.new(carry) if carry > 0 && !prev.nil?
  rev.call(head)
end
