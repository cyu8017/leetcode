// LeetCode 1474 - Delete N Nodes After M Nodes of a Linked List
// https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn delete_nodes(head: Option<Box<ListNode>>, m: i32, n: i32) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode { val: 0, next: head });
        let mut cur = dummy.as_mut();
        loop {
            for _ in 0..m {
                if cur.next.is_none() {
                    return dummy.next;
                }
                cur = cur.next.as_mut().unwrap();
            }
            let mut drop = cur.next.take();
            for _ in 0..n {
                if let Some(node) = drop {
                    drop = node.next;
                } else {
                    break;
                }
            }
            cur.next = drop;
            if cur.next.is_none() {
                break;
            }
        }
        dummy.next
    }
}
