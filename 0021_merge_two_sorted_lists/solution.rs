// LeetCode 0021 - Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/

#[derive(Eq, PartialEq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn merge_two_lists(
        mut list1: Option<Box<ListNode>>,
        mut list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut dummy = ListNode { val: 0, next: None };
        let mut current = &mut dummy;

        while list1.is_some() && list2.is_some() {
            if list1.as_ref().unwrap().val <= list2.as_ref().unwrap().val {
                let next = list1.as_mut().unwrap().next.take();
                current.next = list1.take();
                list1 = next;
            } else {
                let next = list2.as_mut().unwrap().next.take();
                current.next = list2.take();
                list2 = next;
            }
            current = current.next.as_mut().unwrap();
        }

        current.next = if list1.is_some() { list1 } else { list2 };
        dummy.next
    }
}
