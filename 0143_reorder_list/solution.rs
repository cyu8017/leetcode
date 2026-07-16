// LeetCode 0143 - Reorder List
// https://leetcode.com/problems/reorder-list/

// LeetCode 0143 - Reorder List
// https://leetcode.com/problems/reorder-list/

#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl Solution {
    pub fn reorder_list(head: &mut Option<Box<ListNode>>) {
        let mut nodes = Vec::new();
        let mut current = head.take();
        while let Some(mut node) = current {
            current = node.next.take();
            nodes.push(node);
        }

        let mut order = Vec::with_capacity(nodes.len());
        let mut left = 0usize;
        let mut right = nodes.len();
        while left < right {
            order.push(left);
            left += 1;
            if left < right {
                right -= 1;
                order.push(right);
            }
        }

        let mut result = None;
        for index in order.into_iter().rev() {
            let mut node = std::mem::replace(
                &mut nodes[index],
                Box::new(ListNode { val: 0, next: None }),
            );
            node.next = result;
            result = Some(node);
        }
        *head = result;
    }
}