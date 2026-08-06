// LeetCode 1490 - Clone N-ary Tree
// https://leetcode.com/problems/clone-n-ary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub children: Vec<Option<Rc<RefCell<Node>>>>,
}

impl Solution {
    pub fn clone_tree(root: Option<Rc<RefCell<Node>>>) -> Option<Rc<RefCell<Node>>> {
        let root = root?;
        let n = root.borrow();
        Some(Rc::new(RefCell::new(Node {
            val: n.val,
            children: n
                .children
                .iter()
                .map(|c| Self::clone_tree(c.clone()))
                .collect(),
        })))
    }
}
