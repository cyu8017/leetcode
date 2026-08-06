# LeetCode 1474 - Delete N Nodes After M Nodes Of A Linked List
# https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/

def delete_nodes(head, m, n)
  cur = head
  while cur
    (m - 1).times do
      break if cur.nil?
      cur = cur.next
    end
    break if cur.nil?
    drop = cur.next
    n.times { drop = drop.next if drop }
    cur.next = drop
    cur = drop
  end
  head
end
