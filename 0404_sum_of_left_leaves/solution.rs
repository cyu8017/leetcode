// LeetCode 0404 - Sum of Left Leaves
// https://leetcode.com/problems/sum-of-left-leaves/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn sum_of_left_leaves(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let Some(node) = root else {
            return 0;
        };

        let (left, right) = {
            let borrowed = node.borrow();
            (borrowed.left.clone(), borrowed.right.clone())
        };

        let mut total = 0;
        if let Some(left_node) = left {
            let left_borrowed = left_node.borrow();
            if left_borrowed.left.is_none() && left_borrowed.right.is_none() {
                total += left_borrowed.val;
            } else {
                total += Self::sum_of_left_leaves(Some(left_node));
            }
        }

        total += Self::sum_of_left_leaves(right);
        total
    }
}
