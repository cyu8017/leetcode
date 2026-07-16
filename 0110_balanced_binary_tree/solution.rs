// LeetCode 0110 - Balanced Binary Tree
// https://leetcode.com/problems/balanced-binary-tree/

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
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::height(root) != -1
    }

    fn height(node: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match node {
            None => 0,
            Some(node) => {
                let node = node.borrow();
                let left = Self::height(node.left.clone());
                if left == -1 {
                    return -1;
                }
                let right = Self::height(node.right.clone());
                if right == -1 {
                    return -1;
                }
                if (left - right).abs() > 1 {
                    return -1;
                }
                1 + left.max(right)
            }
        }
    }
}
