// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

use std::collections::HashMap;

impl Solution {
    pub fn remove_zero_sum_sublists(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut vals = Vec::new();
        let mut cur = head;
        while let Some(node) = cur {
            vals.push(node.val);
            cur = node.next;
        }
        let mut prefix = 0;
        let mut last = HashMap::new();
        last.insert(0, 0usize);
        for (i, &v) in vals.iter().enumerate() {
            prefix += v;
            last.insert(prefix, i + 1);
        }
        let mut kept = Vec::new();
        let mut i = 0;
        prefix = 0;
        while i < vals.len() {
            let next_prefix = prefix + vals[i];
            let j = *last.get(&next_prefix).unwrap();
            if j == i + 1 {
                kept.push(vals[i]);
                prefix = next_prefix;
                i += 1;
            } else {
                i = j;
            }
        }
        let mut out = None;
        for &v in kept.iter().rev() {
            out = Some(Box::new(ListNode { val: v, next: out }));
        }
        out
    }
}
