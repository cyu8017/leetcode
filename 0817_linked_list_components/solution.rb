# LeetCode 0817 - Linked List Components
# https://leetcode.com/problems/linked-list-components/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

# @param {ListNode} head
# @param {Integer[]} nums
# @return {Integer}
def num_components(head, nums)
  present = nums.each_with_object({}) { |x, h| h[x] = true }
  count = 0
  connected = false
  while head
    if present[head.val]
      unless connected
        count += 1
        connected = true
      end
    else
      connected = false
    end
    head = head.next
  end
  count
end
