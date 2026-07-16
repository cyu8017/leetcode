// LeetCode 0024 - Swap Nodes in Pairs
// https://leetcode.com/problems/swap-nodes-in-pairs/

#[derive(Eq, PartialEq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = ListNode { val: 0, next: head };
        let mut previous = &mut dummy;

        while previous.next.is_some() && previous.next.as_ref().unwrap().next.is_some() {
            let mut first = previous.next.take().unwrap();
            let mut second = first.next.take().unwrap();
            first.next = second.next.take();
            second.next = Some(first);
            previous.next = Some(second);
            previous = previous.next.as_mut().unwrap().next.as_mut().unwrap();
        }

        dummy.next
    }
}
