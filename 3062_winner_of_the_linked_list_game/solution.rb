# LeetCode 3062 - Winner of the Linked List Game
# https://leetcode.com/problems/winner-of-the-linked-list-game/

class ListNode
  attr_accessor :val, :next
  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {String}
def game_result(head)
  odd = 0
  even = 0
  while head
    a = head.val
    b = head.next.val
    odd += 1 if a < b
    even += 1 if a > b
    head = head.next.next
  end
  return "Odd" if odd > even
  return "Even" if odd < even
  "Tie"
end
