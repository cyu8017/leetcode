// LeetCode 0199 - Binary Tree Right Side View
// https://leetcode.com/problems/binary-tree-right-side-view/

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
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut result = Vec::new();
        let mut queue = VecDeque::new();
        if let Some(root) = root {
            queue.push_back(root);
        }

        while !queue.is_empty() {
            let level_size = queue.len();
            for index in 0..level_size {
                let node = queue.pop_front().unwrap();
                let node = node.borrow();
                if index == level_size - 1 {
                    result.push(node.val);
                }
                if let Some(left) = node.left.clone() {
                    queue.push_back(left);
                }
                if let Some(right) = node.right.clone() {
                    queue.push_back(right);
                }
            }
        }
        result
    }
}
