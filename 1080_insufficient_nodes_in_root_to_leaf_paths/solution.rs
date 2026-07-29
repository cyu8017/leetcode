// LeetCode 1080 - Insufficient Nodes in Root to Leaf Paths
// https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

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
    pub fn sufficient_subset(
        root: Option<Rc<RefCell<TreeNode>>>,
        limit: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        Self::dfs(root, 0, limit)
    }

    fn dfs(
        node: Option<Rc<RefCell<TreeNode>>>,
        path_sum: i32,
        limit: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let node = node?;
        let mut borrowed = node.borrow_mut();
        let path_sum = path_sum + borrowed.val;
        if borrowed.left.is_none() && borrowed.right.is_none() {
            drop(borrowed);
            return if path_sum >= limit { Some(node) } else { None };
        }
        borrowed.left = Self::dfs(borrowed.left.take(), path_sum, limit);
        borrowed.right = Self::dfs(borrowed.right.take(), path_sum, limit);
        let keep = borrowed.left.is_some() || borrowed.right.is_some();
        drop(borrowed);
        if keep {
            Some(node)
        } else {
            None
        }
    }
}
