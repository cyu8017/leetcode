
# @param {ListNode} head
# @return {ListNode}
def delete_duplicates_unsorted(head)
  counts = Hash.new(0)
  node = head
  while node
    counts[node.val] += 1
    node = node.next
  end

  dummy = ListNode.new(0)
  dummy.next = head
  prev = dummy
  node = head
  while node
    if counts[node.val] > 1
      prev.next = node.next
      node = node.next
    else
      prev = node
      node = node.next
    end
  end
  dummy.next
end
