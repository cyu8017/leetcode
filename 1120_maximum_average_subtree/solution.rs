// LeetCode 1120 - Maximum Average Subtree
// https://leetcode.com/problems/maximum-average-subtree/

use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    pub fn maximum_average_subtree(root: Option<Rc<RefCell<TreeNode>>>) -> f64 {
        let mut best = 0.0;
        Self::dfs(root, &mut best);
        best
    }

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, best: &mut f64) -> (i32, i32) {
        let node = match node {
            Some(n) => n,
            None => return (0, 0),
        };
        let node = node.borrow();
        let (ls, lc) = Self::dfs(node.left.clone(), best);
        let (rs, rc) = Self::dfs(node.right.clone(), best);
        let total_sum = ls + rs + node.val;
        let total_count = lc + rc + 1;
        *best = best.max(total_sum as f64 / total_count as f64);
        (total_sum, total_count)
    }
}
