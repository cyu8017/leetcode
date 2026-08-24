# LeetCode 2046 - Sort Linked List Already Sorted Using Absolute Values
# https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/

# @param {ListNode} head
# @return {ListNode}
def sort_linked_list(head)
  return nil if head.nil?

  prev = head
  cur = head.next
  while cur
    if cur.val < 0
      prev.next = cur.next
      cur.next = head
      head = cur
      cur = prev.next
    else
      prev = cur
      cur = cur.next
    end
  end
  head
end

def solve(head)
  node = sort_linked_list(head)
  ans = []
  while node
    ans << node.val
    node = node.next
  end
  ans
end
