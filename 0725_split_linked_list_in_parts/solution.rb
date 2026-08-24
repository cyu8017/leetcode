# LeetCode 0725 - Split Linked List in Parts
# https://leetcode.com/problems/split-linked-list-in-parts/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @param {Integer} k
# @return {ListNode[]}
def split_list_to_parts(head, k)
  length = 0
  node = head
  while node
    length += 1
    node = node.next
  end

  part_size, extra = length.divmod(k)
  result = []
  current = head
  k.times do |i|
    result << current
    size = part_size + (i < extra ? 1 : 0)
    (size - 1).times { current = current.next if current }
    if current
      nxt = current.next
      current.next = nil
      current = nxt
    end
  end
  result.map do |part|
    values = []
    while part
      values << part.val
      part = part.next
    end
    values
  end
end
