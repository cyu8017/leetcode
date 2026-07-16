// LeetCode 0061 - Rotate List
// https://leetcode.com/problems/rotate-list/

#[derive(Eq, PartialEq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn rotate_right(mut head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        if head.is_none() || head.as_ref().unwrap().next.is_none() {
            return head;
        }

        let mut length = 0;
        let mut current = head.as_ref();
        while let Some(node) = current {
            length += 1;
            current = node.next.as_ref();
        }

        let k = (k as usize) % length;
        if k == 0 {
            return head;
        }

        let steps = length - k;
        let mut new_tail = head.as_mut().unwrap();
        for _ in 0..steps - 1 {
            new_tail = new_tail.next.as_mut().unwrap();
        }

        let mut new_head = new_tail.next.take();
        let mut tail = new_head.as_mut().unwrap();
        while tail.next.is_some() {
            tail = tail.next.as_mut().unwrap();
        }
        tail.next = head;
        new_head
    }
}
