# LeetCode 2674 - Split a Circular Linked List
# https://leetcode.com/problems/split-a-circular-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} list
# @return {ListNode[]}
def split_circular_linked_list(list)
  return [nil, nil] if list.nil?

  slow = list
  fast = list
  while fast.next != list && fast.next.next != list
    slow = slow.next
    fast = fast.next.next
  end
  fast = fast.next if fast.next.next == list
  head2 = slow.next
  slow.next = list
  fast.next = head2
  [list, head2]
end

def solve(*args)
  split_circular_linked_list(*args)
end
