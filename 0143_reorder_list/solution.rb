class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

# @param {ListNode} head
# @return {void}
def reorder_list(head)
  return if head.nil? || head.next.nil?

  slow = head
  fast = head
  while fast.next && fast.next.next
    slow = slow.next
    fast = fast.next.next
  end

  second = slow.next
  slow.next = nil
  previous = nil
  while second
    next_node = second.next
    second.next = previous
    previous = second
    second = next_node
  end

  first = head
  second = previous
  while second
    first_next = first.next
    second_next = second.next
    first.next = second
    second.next = first_next
    first = first_next
    second = second_next
  end
end