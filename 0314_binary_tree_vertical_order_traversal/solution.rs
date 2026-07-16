// LeetCode 0314 - Binary Tree Vertical Order Traversal
// https://leetcode.com/problems/binary-tree-vertical-order-traversal/

use std::cell::RefCell;
use std::collections::{HashMap, VecDeque};
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
    pub fn vertical_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let Some(root) = root else {
            return Vec::new();
        };

        let mut columns: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut queue = VecDeque::new();
        queue.push_back((root, 0));
        let mut min_col = 0;
        let mut max_col = 0;

        while let Some((node, column)) = queue.pop_front() {
            min_col = min_col.min(column);
            max_col = max_col.max(column);
            let value = node.borrow().val;
            columns.entry(column).or_default().push(value);
            if let Some(left) = node.borrow().left.clone() {
                queue.push_back((left, column - 1));
            }
            if let Some(right) = node.borrow().right.clone() {
                queue.push_back((right, column + 1));
            }
        }

        (min_col..=max_col)
            .map(|column| columns.remove(&column).unwrap_or_default())
            .collect()
    }
}
