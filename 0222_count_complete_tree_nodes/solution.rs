// LeetCode 0222 - Count Complete Tree Nodes
// https://leetcode.com/problems/count-complete-tree-nodes/

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
    pub fn count_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match root {
            None => 0,
            Some(node) => {
                let node = node.borrow();
                let left = Self::left_depth(node.left.clone());
                let right = Self::right_depth(node.right.clone());
                if left == right {
                    (1 << left) - 1
                } else {
                    1 + Self::count_nodes(node.left.clone()) + Self::count_nodes(node.right.clone())
                }
            }
        }
    }

    fn left_depth(mut node: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut depth = 0;
        while let Some(current) = node {
            depth += 1;
            node = current.borrow().left.clone();
        }
        depth
    }

    fn right_depth(mut node: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut depth = 0;
        while let Some(current) = node {
            depth += 1;
            node = current.borrow().right.clone();
        }
        depth
    }
}
