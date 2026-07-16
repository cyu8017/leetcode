# LeetCode 0002 - Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
  dummy = ListNode.new
  current = dummy
  carry = 0

  while l1 || l2 || carry != 0
    total = carry
    if l1
      total += l1.val
      l1 = l1.next
    end
    if l2
      total += l2.val
      l2 = l2.next
    end
    carry, digit = total.divmod(10)
    current.next = ListNode.new(digit)
    current = current.next
  end

  dummy.next
end
