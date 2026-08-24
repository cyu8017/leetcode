// LeetCode 0783 - Minimum Distance Between BST Nodes
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

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
    pub fn min_diff_in_bst(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut prev: Option<i32> = None;
        let mut best = i32::MAX;
        Self::inorder(root, &mut prev, &mut best);
        best
    }

    fn inorder(node: Option<Rc<RefCell<TreeNode>>>, prev: &mut Option<i32>, best: &mut i32) {
        if let Some(node) = node {
            let node = node.borrow();
            Self::inorder(node.left.clone(), prev, best);
            if let Some(p) = *prev {
                *best = (*best).min(node.val - p);
            }
            *prev = Some(node.val);
            Self::inorder(node.right.clone(), prev, best);
        }
    }
}
