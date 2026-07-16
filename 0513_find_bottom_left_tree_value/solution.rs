// LeetCode 0513 - Find Bottom Left Tree Value
// https://leetcode.com/problems/find-bottom-left-tree-value/

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
    pub fn find_bottom_left_value(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let Some(root) = root else {
            return 0;
        };

        let mut queue = VecDeque::new();
        queue.push_back(root);
        let mut leftmost = 0;

        while !queue.is_empty() {
            let level_size = queue.len();
            for index in 0..level_size {
                let node = queue.pop_front().unwrap();
                let node = node.borrow();
                if index == 0 {
                    leftmost = node.val;
                }
                if let Some(left) = node.left.clone() {
                    queue.push_back(left);
                }
                if let Some(right) = node.right.clone() {
                    queue.push_back(right);
                }
            }
        }

        leftmost
    }
}
