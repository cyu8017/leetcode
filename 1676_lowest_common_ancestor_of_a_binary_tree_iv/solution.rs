// LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

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
    pub fn lowest_common_ancestor(
        root: Option<Rc<RefCell<TreeNode>>>,
        nodes: Vec<Option<Rc<RefCell<TreeNode>>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let targets: HashSet<NodePtr> = nodes
            .into_iter()
            .filter_map(|n| n.map(|rc| Rc::as_ptr(&rc)))
            .collect();
        Self::dfs(root, &targets)
    }

    fn dfs(
        node: Option<Rc<RefCell<TreeNode>>>,
        targets: &HashSet<NodePtr>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let node = node?;
        let left = Self::dfs(node.borrow().left.clone(), targets);
        let right = Self::dfs(node.borrow().right.clone(), targets);
        if targets.contains(&Rc::as_ptr(&node)) || (left.is_some() && right.is_some()) {
            Some(node)
        } else {
            left.or(right)
        }
    }
}
