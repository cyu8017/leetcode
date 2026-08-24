struct Solution;
// LeetCode 0572 - Subtree of Another Tree
// https://leetcode.com/problems/subtree-of-another-tree/

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
    fn same(a: &Option<Rc<RefCell<TreeNode>>>, b: &Option<Rc<RefCell<TreeNode>>>) -> bool {
        match (a, b) {
            (None, None) => true,
            (Some(a), Some(b)) => {
                let a = a.borrow();
                let b = b.borrow();
                a.val == b.val && Self::same(&a.left, &b.left) && Self::same(&a.right, &b.right)
            }
            _ => false,
        }
    }

    pub fn is_subtree(
        root: Option<Rc<RefCell<TreeNode>>>,
        sub_root: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        let Some(root) = root else {
            return false;
        };
        let node = root.borrow();
        Self::same(&Some(root.clone()), &sub_root)
            || Self::is_subtree(node.left.clone(), sub_root.clone())
            || Self::is_subtree(node.right.clone(), sub_root)
    }
}

fn main() {}
