// LeetCode 0250 - Count Univalue Subtrees
// https://leetcode.com/problems/count-univalue-subtrees/

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
    pub fn count_univalue_subtrees(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut count = 0;
        Self::dfs(root, &mut count);
        count
    }

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, count: &mut i32) -> bool {
        let Some(node) = node else {
            return true;
        };
        let (left, right, val) = {
            let borrowed = node.borrow();
            (borrowed.left.clone(), borrowed.right.clone(), borrowed.val)
        };
        let left_ok = Self::dfs(left, count);
        let right_ok = Self::dfs(right, count);
        if !left_ok || !right_ok {
            return false;
        }
        let borrowed = node.borrow();
        if borrowed.left.as_ref().is_some_and(|left| left.borrow().val != val) {
            return false;
        }
        if borrowed
            .right
            .as_ref()
            .is_some_and(|right| right.borrow().val != val)
        {
            return false;
        }
        *count += 1;
        true
    }
}
