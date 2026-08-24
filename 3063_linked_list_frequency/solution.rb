# LeetCode 3063 - Linked List Frequency
# https://leetcode.com/problems/linked-list-frequency/

class ListNode
  attr_accessor :val, :next
  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {ListNode}
def frequencies_of_elements(head)
  cnt = Hash.new(0)
  while head
    cnt[head.val] += 1
    head = head.next
  end
  dummy = ListNode.new(0)
  cnt.each_value do |val|
    dummy.next = ListNode.new(val, dummy.next)
  end
  dummy.next
end
