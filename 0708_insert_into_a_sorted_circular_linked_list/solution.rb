# LeetCode 0708 - Insert into a Sorted Circular Linked List
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @param {Integer} insert_val
# @return {ListNode}
def insert(head, insert_val)
  node = ListNode.new(insert_val)
  if head.nil?
    node.next = nil
    return node
  end

  cur = head
  cur = cur.next while cur.next && !cur.next.equal?(head)
  cur.next = head

  prev = head
  curr = head.next
  loop do
    break if prev.val <= insert_val && insert_val <= curr.val
    break if prev.val > curr.val && (insert_val >= prev.val || insert_val <= curr.val)

    prev = curr
    curr = curr.next
    break if prev.equal?(head)
  end

  prev.next = node
  node.next = curr

  # Ruby runner walks until nil; break the cycle after inserting.
  cur = head
  cur = cur.next while cur.next && !cur.next.equal?(head)
  cur.next = nil
  head
end
