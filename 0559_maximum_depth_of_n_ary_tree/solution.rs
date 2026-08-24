// LeetCode 0559 - Maximum Depth of N-ary Tree
// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub children: Vec<Rc<RefCell<Node>>>,
}

impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<Node>>>) -> i32 {
        let Some(root) = root else {
            return 0;
        };
        let node = root.borrow();
        if node.children.is_empty() {
            return 1;
        }
        let mut best = 0;
        for child in &node.children {
            best = best.max(Self::max_depth(Some(child.clone())));
        }
        best + 1
    }
}
