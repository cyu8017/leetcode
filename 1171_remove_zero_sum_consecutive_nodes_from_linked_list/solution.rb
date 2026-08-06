# LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

# @param {ListNode} head
# @return {ListNode}
def remove_zero_sum_sublists(head)
  dummy = Struct.new(:val, :next).new(0, head)
  prefix = 0
  seen = { 0 => dummy }
  node = dummy
  while node
    prefix += node.val
    seen[prefix] = node
    node = node.next
  end
  prefix = 0
  node = dummy
  while node
    prefix += node.val
    node.next = seen[prefix].next
    node = node.next
  end
  dummy.next
end
