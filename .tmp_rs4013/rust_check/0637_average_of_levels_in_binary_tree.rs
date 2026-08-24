struct Solution;
// LeetCode 0637 - Average of Levels in Binary Tree
// https://leetcode.com/problems/average-of-levels-in-binary-tree/

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
use std::collections::VecDeque;

impl Solution {
    pub fn average_of_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<f64> {
        let mut result = Vec::new();
        let Some(root) = root else {
            return result;
        };
        let mut queue = VecDeque::new();
        queue.push_back(root);
        while !queue.is_empty() {
            let count = queue.len();
            let mut total = 0i64;
            for _ in 0..count {
                let node = queue.pop_front().unwrap();
                let node = node.borrow();
                total += node.val as i64;
                if let Some(left) = node.left.clone() {
                    queue.push_back(left);
                }
                if let Some(right) = node.right.clone() {
                    queue.push_back(right);
                }
            }
            result.push(total as f64 / count as f64);
        }
        result
    }
}

fn main() {}
