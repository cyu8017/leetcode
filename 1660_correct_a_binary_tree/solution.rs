// LeetCode 1660 - Correct a Binary Tree
// https://leetcode.com/problems/correct-a-binary-tree/

use std::cell::RefCell;
use std::collections::HashSet;
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

type NodePtr = *const RefCell<TreeNode>;

impl Solution {
    pub fn correct_binary_tree(
        root: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let mut seen: HashSet<NodePtr> = HashSet::new();
        Self::dfs(root, &mut seen)
    }

    fn dfs(
        node: Option<Rc<RefCell<TreeNode>>>,
        seen: &mut HashSet<NodePtr>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let node = node?;
        if let Some(ref right) = node.borrow().right {
            if seen.contains(&Rc::as_ptr(right)) {
                return None;
            }
        }
        seen.insert(Rc::as_ptr(&node));
        let right = node.borrow().right.clone();
        let left = node.borrow().left.clone();
        node.borrow_mut().right = Self::dfs(right, seen);
        node.borrow_mut().left = Self::dfs(left, seen);
        Some(node)
    }
}
