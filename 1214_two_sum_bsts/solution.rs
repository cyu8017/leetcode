// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

use std::cell::RefCell;
use std::collections::HashSet;
use std::rc::Rc;

impl Solution {
    pub fn two_sum_bs_ts(
        root1: Option<Rc<RefCell<TreeNode>>>,
        root2: Option<Rc<RefCell<TreeNode>>>,
        target: i32,
    ) -> bool {
        let mut values = HashSet::new();
        let mut stack = Vec::new();
        if let Some(r) = root1 {
            stack.push(r);
        }
        while let Some(node) = stack.pop() {
            let b = node.borrow();
            values.insert(b.val);
            if let Some(l) = b.left.clone() {
                stack.push(l);
            }
            if let Some(r) = b.right.clone() {
                stack.push(r);
            }
        }
        if let Some(r) = root2 {
            stack.push(r);
        }
        while let Some(node) = stack.pop() {
            let b = node.borrow();
            if values.contains(&(target - b.val)) {
                return true;
            }
            if let Some(l) = b.left.clone() {
                stack.push(l);
            }
            if let Some(r) = b.right.clone() {
                stack.push(r);
            }
        }
        false
    }
}
