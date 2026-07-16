// LeetCode 0107 - Binary Tree Level Order Traversal II
// https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

use std::cell::RefCell;
use std::collections::VecDeque;
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
    pub fn level_order_bottom(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        let Some(root) = root else {
            return result;
        };

        let mut queue = VecDeque::new();
        queue.push_back(root);

        while !queue.is_empty() {
            let size = queue.len();
            let mut level = Vec::with_capacity(size);
            for _ in 0..size {
                let node = queue.pop_front().unwrap();
                let node = node.borrow();
                level.push(node.val);
                if let Some(left) = node.left.clone() {
                    queue.push_back(left);
                }
                if let Some(right) = node.right.clone() {
                    queue.push_back(right);
                }
            }
            result.push(level);
        }

        result.reverse();
        result
    }
}
