// LeetCode 0173 - Binary Search Tree Iterator
// https://leetcode.com/problems/binary-search-tree-iterator/

use std::cell::RefCell;
use std::rc::Rc;

struct BSTIterator {
    stack: Vec<Rc<RefCell<TreeNode>>>,
}

impl BSTIterator {
    fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {
        let mut iterator = Self { stack: Vec::new() };
        iterator.push_left(root);
        iterator
    }

    fn push_left(&mut self, mut node: Option<Rc<RefCell<TreeNode>>>) {
        while let Some(current) = node {
            node = current.borrow().left.clone();
            self.stack.push(current);
        }
    }

    fn next(&mut self) -> i32 {
        let node = self.stack.pop().unwrap();
        let value = node.borrow().val;
        self.push_left(node.borrow().right.clone());
        value
    }

    fn has_next(&self) -> bool {
        !self.stack.is_empty()
    }
}