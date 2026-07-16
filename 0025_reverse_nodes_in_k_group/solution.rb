# LeetCode 0025 - Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next = nil)
    @val = val
    @next = next
  end
end

# @param {ListNode} head
# @param {Integer} k
# @return {ListNode}
def reverse_k_group(head, k)
  values = []
  node = head
  while node
    values << node.val
    node = node.next
  end

  index = 0
  while index + k <= values.length
    values[index, k] = values[index, k].reverse
    index += k
  end

  dummy = ListNode.new
  current = dummy
  values.each do |value|
    current.next = ListNode.new(value)
    current = current.next
  end
  dummy.next
end
