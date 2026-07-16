# LeetCode 0086 - Partition List
# https://leetcode.com/problems/partition-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @param {Integer} x
# @return {ListNode}
def partition(head, x)
  before_head = ListNode.new(0)
  after_head = ListNode.new(0)
  before = before_head
  after = after_head

  while head
    if head.val < x
      before.next = head
      before = before.next
    else
      after.next = head
      after = after.next
    end
    head = head.next
  end

  after.next = nil
  before.next = after_head.next
  before_head.next
end
