// LeetCode 0019 - Remove Nth Node From End of List
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

#[derive(Eq, PartialEq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode { val: 0, next: head });

        let mut length = 0;
        let mut current = dummy.next.as_ref();
        while current.is_some() {
            length += 1;
            current = current.unwrap().next.as_ref();
        }

        let remove_at = length - n as usize;
        let mut node = dummy.as_mut();
        for _ in 0..remove_at {
            node = node.next.as_mut().unwrap();
        }

        let next = node.next.as_mut().unwrap().next.take();
        node.next = next;
        dummy.next
    }
}
