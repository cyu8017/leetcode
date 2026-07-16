// LeetCode 0298 - Binary Tree Longest Consecutive Sequence
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn longest_consecutive(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(
            node: Option<Rc<RefCell<TreeNode>>>,
            parent: Option<Rc<RefCell<TreeNode>>>,
            length: i32,
        ) -> i32 {
            let Some(node) = node else {
                return 0;
            };

            let node_val = node.borrow().val;
            let current = if parent
                .as_ref()
                .map(|parent| parent.borrow().val + 1 == node_val)
                .unwrap_or(false)
            {
                length + 1
            } else {
                1
            };

            current
                .max(dfs(
                    node.borrow().left.clone(),
                    Some(node.clone()),
                    current,
                ))
                .max(dfs(
                    node.borrow().right.clone(),
                    Some(node.clone()),
                    current,
                ))
        }

        dfs(root, None, 0)
    }
}
