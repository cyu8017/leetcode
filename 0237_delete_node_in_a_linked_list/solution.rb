# LeetCode 0237 - Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next = nil)
    @val = val
    @next = next
  end
end

# @param {ListNode} node
# @return {void}
def delete_node(node)
  node.val = node.next.val
  node.next = node.next.next
end
