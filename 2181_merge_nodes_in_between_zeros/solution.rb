# LeetCode 2181 - Merge Nodes in Between Zeros
# https://leetcode.com/problems/merge-nodes-in-between-zeros/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {ListNode}
def merge_nodes(head)
  dummy = ListNode.new
  cur = dummy
  sum = 0
  p = head.next
  while p
    if p.val == 0
      cur.next = ListNode.new(sum)
      cur = cur.next
      sum = 0
    else
      sum += p.val
    end
    p = p.next
  end
  dummy.next
end
