// LeetCode 0515 - Find Largest Value in Each Tree Row
// https://leetcode.com/problems/find-largest-value-in-each-tree-row/

use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn largest_values(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let Some(root) = root else {
            return Vec::new();
        };

        let mut result = Vec::new();
        let mut queue = VecDeque::new();
        queue.push_back(root);

        while !queue.is_empty() {
            let level_size = queue.len();
            let mut level_max = i32::MIN;
            for _ in 0..level_size {
                let node = queue.pop_front().unwrap();
                let node = node.borrow();
                level_max = level_max.max(node.val);
                if let Some(left) = node.left.clone() {
                    queue.push_back(left);
                }
                if let Some(right) = node.right.clone() {
                    queue.push_back(right);
                }
            }
            result.push(level_max);
        }

        result
    }
}
