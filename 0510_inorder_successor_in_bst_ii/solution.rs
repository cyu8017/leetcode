// LeetCode 0510 - Inorder Successor in BST II
// https://leetcode.com/problems/inorder-successor-in-bst-ii/

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
    pub fn inorder_successor(node: Option<Rc<RefCell<Node>>>) -> Option<Rc<RefCell<Node>>> {
        let node = node.unwrap();
        if node.borrow().right.is_some() {
            let mut current = node.borrow().right.clone();
            loop {
                let Some(curr) = current.clone() else {
                    break;
                };
                if curr.borrow().left.is_some() {
                    current = curr.borrow().left.clone();
                } else {
                    return current;
                }
            }
        }

        let mut current = Some(node);
        while let Some(curr) = current.clone() {
            let Some(parent) = curr.borrow().parent.clone() else {
                return None;
            };
            let is_right_child = parent
                .borrow()
                .right
                .as_ref()
                .map_or(false, |right| Rc::ptr_eq(right, &curr));
            if !is_right_child {
                return Some(parent);
            }
            current = Some(parent);
        }
        None
    }
}
