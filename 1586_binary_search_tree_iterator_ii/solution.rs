// LeetCode 1586 - Binary Search Tree Iterator II
// https://leetcode.com/problems/binary-search-tree-iterator-ii/

use std::cell::RefCell;
use std::rc::Rc;

pub struct BSTIterator {
    values: Vec<i32>,
    index: i32,
}

impl BSTIterator {
    pub fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {
        let mut values = Vec::new();
        let mut stack = Vec::new();
        let mut cur = root;
        while !stack.is_empty() || cur.is_some() {
            while let Some(node) = cur {
                stack.push(node.clone());
                cur = node.borrow().left.clone();
            }
            let node = stack.pop().unwrap();
            values.push(node.borrow().val);
            cur = node.borrow().right.clone();
        }
        Self { values, index: -1 }
    }

    pub fn has_next(&self) -> bool {
        (self.index + 1) < self.values.len() as i32
    }

    pub fn next(&mut self) -> i32 {
        self.index += 1;
        self.values[self.index as usize]
    }

    pub fn has_prev(&self) -> bool {
        self.index > 0
    }

    pub fn prev(&mut self) -> i32 {
        self.index -= 1;
        self.values[self.index as usize]
    }
}
