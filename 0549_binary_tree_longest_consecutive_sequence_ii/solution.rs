// LeetCode 0549 - Binary Tree Longest Consecutive Sequence II
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

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
        let mut best = 0;

        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, best: &mut i32) -> (i32, i32) {
            let Some(node) = node else {
                return (0, 0);
            };

            let (left_inc, left_dec) = dfs(node.borrow().left.clone(), best);
            let (right_inc, right_dec) = dfs(node.borrow().right.clone(), best);

            let node_val = node.borrow().val;
            let mut inc = 1;
            let mut dec = 1;

            if let Some(left) = node.borrow().left.clone() {
                let left_val = left.borrow().val;
                if left_val == node_val + 1 {
                    inc = inc.max(left_inc + 1);
                } else if left_val == node_val - 1 {
                    dec = dec.max(left_dec + 1);
                }
            }
            if let Some(right) = node.borrow().right.clone() {
                let right_val = right.borrow().val;
                if right_val == node_val + 1 {
                    inc = inc.max(right_inc + 1);
                } else if right_val == node_val - 1 {
                    dec = dec.max(right_dec + 1);
                }
            }

            if let (Some(left), Some(right)) =
                (node.borrow().left.clone(), node.borrow().right.clone())
            {
                let left_val = left.borrow().val;
                let right_val = right.borrow().val;
                if left_val + 1 == node_val && node_val + 1 == right_val {
                    *best = (*best).max(left_dec + 1 + right_inc);
                }
                if left_val - 1 == node_val && node_val - 1 == right_val {
                    *best = (*best).max(left_inc + 1 + right_dec);
                }
            }

            *best = (*best).max(inc).max(dec);
            (inc, dec)
        }

        dfs(root, &mut best);
        best
    }
}
