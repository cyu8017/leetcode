class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

# @param {ListNode} head
# @return {ListNode}
def sort_list(head)
  return head if head.nil? || head.next.nil?

  slow = head
  fast = head
  previous = nil
  while fast && fast.next
    previous = slow
    slow = slow.next
    fast = fast.next.next
  end
  previous.next = nil

  merge(sort_list(head), sort_list(slow))
end

def merge(left, right)
  dummy = ListNode.new(0)
  tail = dummy
  while left && right
    if left.val <= right.val
      tail.next = left
      left = left.next
    else
      tail.next = right
      right = right.next
    end
    tail = tail.next
  end
  tail.next = left || right
  dummy.next
end