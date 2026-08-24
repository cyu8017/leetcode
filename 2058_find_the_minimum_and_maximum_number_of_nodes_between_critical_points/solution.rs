// LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

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
    pub fn nodes_between_critical_points(head: Option<Box<ListNode>>) -> Vec<i32> {
        let mut vals = Vec::new();
        let mut cur = head.as_ref();
        while let Some(n) = cur {
            vals.push(n.val);
            cur = n.next.as_ref();
        }
        let mut crit = Vec::new();
        for i in 1..vals.len().saturating_sub(1) {
            if (vals[i] > vals[i - 1] && vals[i] > vals[i + 1])
                || (vals[i] < vals[i - 1] && vals[i] < vals[i + 1])
            {
                crit.push(i as i32);
            }
        }
        if crit.len() < 2 {
            return vec![-1, -1];
        }
        let mut mn = crit[1] - crit[0];
        for i in 2..crit.len() {
            mn = mn.min(crit[i] - crit[i - 1]);
        }
        vec![mn, crit[crit.len() - 1] - crit[0]]
    }
}
