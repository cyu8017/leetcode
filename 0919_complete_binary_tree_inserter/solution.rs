// LeetCode 0919 - Complete Binary Tree Inserter
// https://leetcode.com/problems/complete-binary-tree-inserter/

use std::cell::RefCell;
use std::collections::VecDeque;
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

pub struct CBTInserter {
    root: Option<Rc<RefCell<TreeNode>>>,
    parents: VecDeque<Rc<RefCell<TreeNode>>>,
}

impl CBTInserter {
    pub fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {
        let root_node = root.clone().unwrap();
        let mut parents = VecDeque::new();
        let mut q = VecDeque::new();
        q.push_back(root_node.clone());
        let mut stopped = false;
        while let Some(node) = q.pop_front() {
            let left = node.borrow().left.clone();
            let right = node.borrow().right.clone();
            if !stopped {
                if let Some(l) = left {
                    q.push_back(l);
                } else {
                    parents.push_back(node.clone());
                    stopped = true;
                    continue;
                }
                if let Some(r) = right {
                    q.push_back(r);
                } else {
                    parents.push_back(node.clone());
                    stopped = true;
                    continue;
                }
            } else {
                parents.push_back(node);
            }
        }
        Self {
            root,
            parents,
        }
    }

    pub fn insert(&mut self, val: i32) -> i32 {
        let parent = self.parents.front().unwrap().clone();
        let child = Rc::new(RefCell::new(TreeNode::new(val)));
        let parent_val = parent.borrow().val;
        if parent.borrow().left.is_none() {
            parent.borrow_mut().left = Some(child.clone());
        } else {
            parent.borrow_mut().right = Some(child.clone());
            self.parents.pop_front();
        }
        self.parents.push_back(child);
        parent_val
    }

    pub fn get_root(&self) -> Option<Rc<RefCell<TreeNode>>> {
        self.root.clone()
    }
}
