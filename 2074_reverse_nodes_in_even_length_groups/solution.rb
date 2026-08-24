# LeetCode 2074 - Reverse Nodes in Even Length Groups
# https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {ListNode}
def reverse_even_length_groups(head)
  dummy = ListNode.new(0, head)
  prev = dummy
  group = 1
  while prev.next
    cur = prev.next
    cnt = 0
    node = cur
    while node && cnt < group
      node = node.next
      cnt += 1
    end
    if cnt.even?
      rev_prev = node
      p = cur
      cnt.times do
        nxt = p.next
        p.next = rev_prev
        rev_prev = p
        p = nxt
      end
      prev.next = rev_prev
      prev = cur
    else
      cnt.times { prev = prev.next }
    end
    group += 1
  end
  dummy.next
end
