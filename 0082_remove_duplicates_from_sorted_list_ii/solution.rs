// LeetCode 0082 - Remove Duplicates from Sorted List II
// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

#[derive(Eq, PartialEq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = ListNode { val: 0, next: head };
        let mut previous = &mut dummy;

        while let Some(mut current) = previous.next.take() {
            let val = current.val;
            if current.next.as_ref().map_or(false, |n| n.val == val) {
                while current.next.as_ref().map_or(false, |n| n.val == val) {
                    current = current.next.take().unwrap();
                }
                previous.next = current.next.take();
            } else {
                previous.next = Some(current);
                previous = previous.next.as_mut().unwrap();
            }
        }

        dummy.next
    }
}
