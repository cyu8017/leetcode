// LeetCode 0687 - Longest Univalue Path
// https://leetcode.com/problems/longest-univalue-path/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

impl Solution {
    pub fn longest_univalue_path(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut best = 0;
        Self::dfs(root, &mut best);
        best
    }

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, best: &mut i32) -> i32 {
        let Some(node) = node else {
            return 0;
        };
        let node = node.borrow();
        let left = Self::dfs(node.left.clone(), best);
        let right = Self::dfs(node.right.clone(), best);
        let left_path = if node.left.as_ref().map_or(false, |c| c.borrow().val == node.val) {
            left + 1
        } else {
            0
        };
        let right_path = if node.right.as_ref().map_or(false, |c| c.borrow().val == node.val) {
            right + 1
        } else {
            0
        };
        *best = (*best).max(left_path + right_path);
        left_path.max(right_path)
    }
}
