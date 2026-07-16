// LeetCode 0333 - Largest BST Subtree
// https://leetcode.com/problems/largest-bst-subtree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn largest_bst_subtree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut best = 0;
        Self::dfs(root, &mut best);
        best
    }

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, best: &mut i32) -> (bool, i32, i32, i32) {
        let Some(node) = node else {
            return (true, i32::MAX, i32::MIN, 0);
        };

        let (left, right, val) = {
            let borrowed = node.borrow();
            (
                borrowed.left.clone(),
                borrowed.right.clone(),
                borrowed.val,
            )
        };

        let (left_ok, left_min, left_max, left_size) = Self::dfs(left, best);
        let (right_ok, right_min, right_max, right_size) = Self::dfs(right, best);

        if left_ok && right_ok && left_max < val && val < right_min {
            let size = left_size + right_size + 1;
            *best = (*best).max(size);
            return (true, left_min.min(val), right_max.max(val), size);
        }

        (false, 0, 0, 0)
    }
}
