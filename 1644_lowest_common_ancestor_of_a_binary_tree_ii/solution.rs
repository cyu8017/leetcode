// LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

use std::cell::RefCell;
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
        TreeNode { val, left: None, right: None }
    }
}

impl Solution {
    pub fn lowest_common_ancestor(
        root: Option<Rc<RefCell<TreeNode>>>,
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let p_val = p.as_ref()?.borrow().val;
        let q_val = q.as_ref()?.borrow().val;
        let mut found = 0;
        let ans = Self::dfs(&root, p_val, q_val, &mut found);
        if found == 2 {
            ans
        } else {
            None
        }
    }

    fn dfs(
        node: &Option<Rc<RefCell<TreeNode>>>,
        p: i32,
        q: i32,
        found: &mut i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let Some(node) = node else { return None };
        let left = Self::dfs(&node.borrow().left, p, q, found);
        let right = Self::dfs(&node.borrow().right, p, q, found);
        let val = node.borrow().val;
        if val == p || val == q {
            *found += 1;
            return Some(node.clone());
        }
        match (left, right) {
            (Some(_), Some(_)) => Some(node.clone()),
            (Some(l), None) => Some(l),
            (None, Some(r)) => Some(r),
            _ => None,
        }
    }
}
