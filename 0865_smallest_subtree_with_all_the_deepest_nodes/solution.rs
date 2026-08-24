// LeetCode 0865 - Smallest Subtree with all the Deepest Nodes
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

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
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

impl Solution {
    pub fn subtree_with_all_deepest(
        root: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        Self::dfs(root).1
    }

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>) -> (i32, Option<Rc<RefCell<TreeNode>>>) {
        let Some(node) = node else {
            return (0, None);
        };
        let borrowed = node.borrow();
        let (ld, ln) = Self::dfs(borrowed.left.clone());
        let (rd, rn) = Self::dfs(borrowed.right.clone());
        drop(borrowed);
        if ld > rd {
            (ld + 1, ln)
        } else if rd > ld {
            (rd + 1, rn)
        } else {
            (ld + 1, Some(node))
        }
    }
}
