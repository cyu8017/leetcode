// LeetCode 0328 - Odd Even Linked List
// https://leetcode.com/problems/odd-even-linked-list/

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        Self { val, next: None }
    }
}

impl Solution {
    pub fn odd_even_list(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.as_ref().map_or(true, |node| node.next.is_none()) {
            return head;
        }

        let mut odd = head.as_mut();
        let mut even_head = odd.as_mut().unwrap().next.take();
        let mut even = even_head.as_mut();

        while even.as_ref().and_then(|node| node.next.as_ref()).is_some() {
            odd.as_mut().unwrap().next = even.as_mut().unwrap().next.take();
            odd = odd.as_mut().unwrap().next.as_mut();
            even.as_mut().unwrap().next = odd.as_mut().unwrap().next.take();
            even = even.as_mut().unwrap().next.as_mut();
        }

        odd.as_mut().unwrap().next = even_head;
        head
    }
}
