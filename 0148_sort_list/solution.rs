// LeetCode 0148 - Sort List
// https://leetcode.com/problems/sort-list/

// LeetCode 0148 - Sort List
// https://leetcode.com/problems/sort-list/

#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn sort_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut values = Vec::new();
        let mut current = head;
        while let Some(node) = current {
            values.push(node.val);
            current = node.next;
        }
        values.sort_unstable();

        let mut result = None;
        for value in values.into_iter().rev() {
            result = Some(Box::new(ListNode { val: value, next: result }));
        }
        result
    }
}