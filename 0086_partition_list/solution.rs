// LeetCode 0086 - Partition List
// https://leetcode.com/problems/partition-list/

#[derive(Eq, PartialEq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn partition(mut head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
        let mut before_dummy = ListNode { val: 0, next: None };
        let mut after_dummy = ListNode { val: 0, next: None };
        let mut before = &mut before_dummy;
        let mut after = &mut after_dummy;

        while let Some(mut node) = head {
            head = node.next.take();
            if node.val < x {
                before.next = Some(node);
                before = before.next.as_mut().unwrap();
            } else {
                after.next = Some(node);
                after = after.next.as_mut().unwrap();
            }
        }

        before.next = after_dummy.next;
        before_dummy.next
    }
}
