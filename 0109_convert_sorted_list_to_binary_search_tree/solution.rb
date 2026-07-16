# LeetCode 0109 - Convert Sorted List to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {ListNode} head
# @return {TreeNode}
def sorted_list_to_bst(head)
  values = []
  while head
    values << head.val
    head = head.next
  end

  build = lambda do |left, right|
    return nil if left > right

    mid = (left + right + 1) / 2
    root = TreeNode.new(values[mid])
    root.left = build.call(left, mid - 1)
    root.right = build.call(mid + 1, right)
    root
  end

  build.call(0, values.length - 1)
end
