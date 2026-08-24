struct Solution;
// LeetCode 0662 - Maximum Width of Binary Tree
// https://leetcode.com/problems/maximum-width-of-binary-tree/

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
    pub fn width_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let Some(root) = root else {
            return 0;
        };
        let mut queue = VecDeque::new();
        queue.push_back((root, 0u64));
        let mut best = 0i32;
        while !queue.is_empty() {
            let left = queue.front().unwrap().1;
            let size = queue.len();
            for _ in 0..size {
                let (node, idx) = queue.pop_front().unwrap();
                best = best.max((idx - left + 1) as i32);
                let node = node.borrow();
                if let Some(left_child) = node.left.clone() {
                    queue.push_back((left_child, idx * 2));
                }
                if let Some(right_child) = node.right.clone() {
                    queue.push_back((right_child, idx * 2 + 1));
                }
            }
        }
        best
    }
}

fn main() {}
