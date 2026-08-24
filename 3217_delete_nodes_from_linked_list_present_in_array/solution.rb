# LeetCode 3217 - Delete Nodes From Linked List Present in Array
# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

class ListNode
  attr_accessor :val, :next
  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {Integer[]} nums
# @param {ListNode} head
# @return {ListNode}
def modified_list(nums, head)
  s = {}
  nums.each { |x| s[x] = true }
  dummy = ListNode.new(0, head)
  pre = dummy
  while pre.next
    if s[pre.next.val]
      pre.next = pre.next.next
    else
      pre = pre.next
    end
  end
  dummy.next
end
