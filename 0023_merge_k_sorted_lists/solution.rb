# LeetCode 0023 - Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next = nil)
    @val = val
    @next = next
  end
end

# @param {ListNode[]} lists
# @return {ListNode}
def merge_k_lists(lists)
  heap = []
  lists.each do |node|
    next if node.nil?

    heap << [node.val, node]
    heap.sort_by!(&:first)
  end

  dummy = ListNode.new
  current = dummy

  until heap.empty?
    heap.sort_by!(&:first)
    _, node = heap.shift
    current.next = node
    current = current.next
    if node.next
      heap << [node.next.val, node.next]
    end
  end

  dummy.next
end
