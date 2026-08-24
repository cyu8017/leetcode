// LeetCode 2095 - Delete the Middle Node of a Linked List
// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn delete_middle(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut head = head;
        if head.as_ref()?.next.is_none() {
            return None;
        }
        let mut n = 0;
        {
            let mut cur = head.as_ref();
            while let Some(node) = cur {
                n += 1;
                cur = node.next.as_ref();
            }
        }
        let mid = n / 2;
        let mut dummy = ListNode { val: 0, next: head };
        let mut cur = &mut dummy;
        for _ in 0..mid {
            cur = cur.next.as_mut().unwrap();
        }
        let nxt = cur.next.take();
        cur.next = nxt.and_then(|node| node.next);
        dummy.next
    }
}
