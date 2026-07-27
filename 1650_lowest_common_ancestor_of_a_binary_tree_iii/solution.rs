// LeetCode 1650 - Lowest Common Ancestor of a Binary Tree III
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub left: Option<Rc<RefCell<Node>>>,
    pub right: Option<Rc<RefCell<Node>>>,
    pub parent: Option<Rc<RefCell<Node>>>,
}

impl Solution {
    pub fn lowest_common_ancestor(
        p: Option<Rc<RefCell<Node>>>,
        q: Option<Rc<RefCell<Node>>>,
    ) -> Option<Rc<RefCell<Node>>> {
        let mut a = p.clone();
        let mut b = q.clone();
        while !Self::same(&a, &b) {
            a = if let Some(ref node) = a {
                node.borrow().parent.clone()
            } else {
                q.clone()
            };
            b = if let Some(ref node) = b {
                node.borrow().parent.clone()
            } else {
                p.clone()
            };
        }
        a
    }

    fn same(a: &Option<Rc<RefCell<Node>>>, b: &Option<Rc<RefCell<Node>>>) -> bool {
        match (a, b) {
            (None, None) => true,
            (Some(x), Some(y)) => Rc::ptr_eq(x, y),
            _ => false,
        }
    }
}
