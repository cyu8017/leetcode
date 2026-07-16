// LeetCode 0147 - Insertion Sort List
// https://leetcode.com/problems/insertion-sort-list/

// LeetCode 0147 - Insertion Sort List
// https://leetcode.com/problems/insertion-sort-list/

#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn insertion_sort_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut sorted: Option<Box<ListNode>> = None;
        let mut current = head;
        while let Some(mut node) = current {
            current = node.next.take();
            let mut link = &mut sorted;
            while link.as_ref().is_some_and(|next| next.val < node.val) {
                link = &mut link.as_mut().unwrap().next;
            }
            node.next = link.take();
            *link = Some(node);
        }
        sorted
    }
}