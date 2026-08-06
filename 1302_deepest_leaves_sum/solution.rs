// LeetCode 1302 - Deepest Leaves Sum
// https://leetcode.com/problems/deepest-leaves-sum/

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
    pub fn deepest_leaves_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut level = vec![root.unwrap()];
        let mut answer = 0;
        while !level.is_empty() {
            answer = level.iter().map(|n| n.borrow().val).sum();
            let mut next = Vec::new();
            for node in level {
                let n = node.borrow();
                if let Some(left) = n.left.clone() {
                    next.push(left);
                }
                if let Some(right) = n.right.clone() {
                    next.push(right);
                }
            }
            level = next;
        }
        answer
    }
}
