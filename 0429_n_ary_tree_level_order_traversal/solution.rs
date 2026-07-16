// LeetCode 0429 - N-ary Tree Level Order Traversal
// https://leetcode.com/problems/n-ary-tree-level-order-traversal/

use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub children: Vec<Rc<RefCell<Node>>>,
}

impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<Node>>>) -> Vec<Vec<i32>> {
        let Some(root) = root else {
            return Vec::new();
        };

        let mut result = Vec::new();
        let mut queue = VecDeque::new();
        queue.push_back(root);

        while !queue.is_empty() {
            let size = queue.len();
            let mut level = Vec::with_capacity(size);
            for _ in 0..size {
                let node = queue.pop_front().unwrap();
                let node = node.borrow();
                level.push(node.val);
                for child in &node.children {
                    queue.push_back(child.clone());
                }
            }
            result.push(level);
        }

        result
    }
}
