// LeetCode 0092 - Reverse Linked List II
// https://leetcode.com/problems/reverse-linked-list-ii/

#[derive(Eq, PartialEq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn reverse_between(
        head: Option<Box<ListNode>>,
        left: i32,
        right: i32,
    ) -> Option<Box<ListNode>> {
        if head.is_none() || left == right {
            return head;
        }

        let mut dummy = Some(Box::new(ListNode { val: 0, next: head }));
        let mut pred = &mut dummy;
        for _ in 1..left {
            pred = &mut pred.as_mut().unwrap().next;
        }

        let mut curr = pred.as_mut().unwrap().next.take();
        let mut reversed: Option<Box<ListNode>> = None;
        for _ in 0..=(right - left) {
            let mut node = curr.unwrap();
            curr = node.next.take();
            node.next = reversed;
            reversed = Some(node);
        }

        let mut tail = &mut reversed;
        while tail.as_ref().unwrap().next.is_some() {
            tail = &mut tail.as_mut().unwrap().next;
        }
        tail.as_mut().unwrap().next = curr;
        pred.as_mut().unwrap().next = reversed;

        dummy.unwrap().next
    }
}
