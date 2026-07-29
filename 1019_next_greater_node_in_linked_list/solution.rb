# LeetCode 1019 - Next Greater Node In Linked List
# https://leetcode.com/problems/next-greater-node-in-linked-list/

# @param {ListNode} head
# @return {Integer[]}
def next_larger_nodes(head)
  vals = []
  while head
    vals << head.val
    head = head.next
  end
  ans = Array.new(vals.length, 0)
  stack = []
  vals.each_with_index do |x, i|
    while !stack.empty? && vals[stack[-1]] < x
      ans[stack.pop] = x
    end
    stack << i
  end
  ans
end
