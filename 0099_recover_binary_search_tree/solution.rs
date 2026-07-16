// LeetCode 0099 - Recover Binary Search Tree
// https://leetcode.com/problems/recover-binary-search-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn recover_tree(root: &mut Option<Rc<RefCell<TreeNode>>>) {
        let mut first: Option<Rc<RefCell<TreeNode>>> = None;
        let mut second: Option<Rc<RefCell<TreeNode>>> = None;
        let mut previous: Option<Rc<RefCell<TreeNode>>> = None;
        let mut stack: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
        let mut current = root.clone();

        while current.is_some() || !stack.is_empty() {
            while let Some(node) = current {
                stack.push(Rc::clone(&node));
                current = node.borrow().left.clone();
            }
            let node = stack.pop().unwrap();
            {
                let node_ref = node.borrow();
                if let Some(prev) = previous.as_ref() {
                    if prev.borrow().val > node_ref.val {
                        if first.is_none() {
                            first = Some(Rc::clone(prev));
                        }
                        second = Some(Rc::clone(&node));
                    }
                }
            }
            previous = Some(Rc::clone(&node));
            current = node.borrow().right.clone();
        }

        if let (Some(a), Some(b)) = (first, second) {
            let mut a_mut = a.borrow_mut();
            let mut b_mut = b.borrow_mut();
            std::mem::swap(&mut a_mut.val, &mut b_mut.val);
        }
    }
}
