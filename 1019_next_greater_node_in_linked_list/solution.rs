// LeetCode 1019 - Next Greater Node In Linked List
// https://leetcode.com/problems/next-greater-node-in-linked-list/

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    pub fn next_larger_nodes(head: Option<Box<ListNode>>) -> Vec<i32> {
        let mut vals = Vec::new();
        let mut cur = head;
        while let Some(node) = cur {
            vals.push(node.val);
            cur = node.next;
        }
        let mut ans = vec![0; vals.len()];
        let mut stack: Vec<usize> = Vec::new();
        for (i, &x) in vals.iter().enumerate() {
            while let Some(&j) = stack.last() {
                if vals[j] < x {
                    ans[stack.pop().unwrap()] = x;
                } else {
                    break;
                }
            }
            stack.push(i);
        }
        ans
    }
}
