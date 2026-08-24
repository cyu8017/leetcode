struct Solution;
// LeetCode 0563 - Binary Tree Tilt
// https://leetcode.com/problems/binary-tree-tilt/

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
    fn subtree_sum(node: &Option<Rc<RefCell<TreeNode>>>, total: &mut i32) -> i32 {
        let Some(node) = node else {
            return 0;
        };
        let node = node.borrow();
        let left = Self::subtree_sum(&node.left, total);
        let right = Self::subtree_sum(&node.right, total);
        *total += (left - right).abs();
        node.val + left + right
    }

    pub fn find_tilt(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut total = 0;
        Self::subtree_sum(&root, &mut total);
        total
    }
}

fn main() {}
