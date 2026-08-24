# LeetCode 2807 - Insert Greatest Common Divisors in Linked List
# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {ListNode}
def insert_greatest_common_divisors(head)
  gcd = lambda do |a, b|
    a, b = b, a % b while b != 0
    a
  end
  cur = head
  while cur && cur.next
    g = gcd.call(cur.val, cur.next.val)
    node = ListNode.new(g, cur.next)
    cur.next = node
    cur = node.next
  end
  head
end
