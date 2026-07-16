# LeetCode 0083 - Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {ListNode}
def delete_duplicates(head)
  current = head

  while current && current.next
    if current.val == current.next.val
      current.next = current.next.next
    else
      current = current.next
    end
  end

  head
end
