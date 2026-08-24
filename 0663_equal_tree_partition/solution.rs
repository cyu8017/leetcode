// LeetCode 0663 - Equal Tree Partition
// https://leetcode.com/problems/equal-tree-partition/

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
    fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, sums: &mut Vec<i32>) -> i32 {
        let Some(node) = node else {
            return 0;
        };
        let node = node.borrow();
        let total = node.val + Self::dfs(&node.left, sums) + Self::dfs(&node.right, sums);
        sums.push(total);
        total
    }

    pub fn check_equal_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut subtree_sums = Vec::new();
        let total = Self::dfs(&root, &mut subtree_sums);
        if !subtree_sums.is_empty() {
            subtree_sums.pop();
        }
        if total % 2 != 0 {
            return false;
        }
        let half = total / 2;
        subtree_sums.iter().any(|&s| s == half)
    }
}
