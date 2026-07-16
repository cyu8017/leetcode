class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

# @param {ListNode} head
# @return {ListNode}
def insertion_sort_list(head)
  dummy = ListNode.new(0)
  current = head

  while current
    previous = dummy
    previous = previous.next while previous.next && previous.next.val < current.val
    next_node = current.next
    current.next = previous.next
    previous.next = current
    current = next_node
  end

  dummy.next
end