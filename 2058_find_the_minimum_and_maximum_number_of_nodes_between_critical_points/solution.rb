# LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {ListNode} head
# @return {Integer[]}
def nodes_between_critical_points(head)
  crit = []
  prev = head
  cur = head.next
  idx = 1
  while cur && cur.next
    if (cur.val > prev.val && cur.val > cur.next.val) || (cur.val < prev.val && cur.val < cur.next.val)
      crit << idx
    end
    prev = cur
    cur = cur.next
    idx += 1
  end
  return [-1, -1] if crit.length < 2

  mn = crit[1] - crit[0]
  (2...crit.length).each { |i| mn = [mn, crit[i] - crit[i - 1]].min }
  [mn, crit[-1] - crit[0]]
end
