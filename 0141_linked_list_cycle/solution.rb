class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

# @param {ListNode} head
# @return {Boolean}
def has_cycle(head)
  slow = head
  fast = head

  while fast && fast.next
    slow = slow.next
    fast = fast.next.next
    return true if slow.equal?(fast)
  end

  false
end