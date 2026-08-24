// LeetCode 0653 - Two Sum IV - Input is a BST
// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

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
use std::collections::HashSet;

impl Solution {
    fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, k: i32, seen: &mut HashSet<i32>) -> bool {
        let Some(node) = node else {
            return false;
        };
        let node = node.borrow();
        if seen.contains(&(k - node.val)) {
            return true;
        }
        seen.insert(node.val);
        Self::dfs(&node.left, k, seen) || Self::dfs(&node.right, k, seen)
    }

    pub fn find_target(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> bool {
        let mut seen = HashSet::new();
        Self::dfs(&root, k, &mut seen)
    }
}
