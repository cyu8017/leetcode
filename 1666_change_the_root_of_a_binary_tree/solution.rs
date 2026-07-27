// LeetCode 1666 - Change the Root of a Binary Tree
// https://leetcode.com/problems/change-the-root-of-a-binary-tree/

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
    pub fn flip_binary_tree(
        root: Option<Rc<RefCell<Node>>>,
        leaf: Option<Rc<RefCell<Node>>>,
    ) -> Option<Rc<RefCell<Node>>> {
        let root = root?;
        let leaf = leaf?;
        let mut node = leaf.clone();
        while !Rc::ptr_eq(&node, &root) {
            let parent = node.borrow().parent.clone().unwrap();
            {
                let mut p = parent.borrow_mut();
                if p.left.as_ref().map_or(false, |l| Rc::ptr_eq(l, &node)) {
                    p.left = None;
                } else {
                    p.right = None;
                }
            }
            let original_left = node.borrow().left.clone();
            node.borrow_mut().left = Some(parent.clone());
            if original_left.is_some() {
                node.borrow_mut().right = original_left;
            }
            node = parent;
        }
        Self::fix_parent(Some(leaf.clone()), None);
        Some(leaf)
    }

    fn fix_parent(cur: Option<Rc<RefCell<Node>>>, parent: Option<Rc<RefCell<Node>>>) {
        let Some(cur) = cur else {
            return;
        };
        cur.borrow_mut().parent = parent;
        let left = cur.borrow().left.clone();
        let right = cur.borrow().right.clone();
        Self::fix_parent(left, Some(cur.clone()));
        Self::fix_parent(right, Some(cur));
    }
}
