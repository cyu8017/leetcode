class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

# @param {ListNode} head
# @return {ListNode}
def detect_cycle(head)
  slow = head
  fast = head

  while fast && fast.next
    slow = slow.next
    fast = fast.next.next
    next unless slow.equal?(fast)

    slow = head
    until slow.equal?(fast)
      slow = slow.next
      fast = fast.next
    end
    return slow
  end

  nil
end