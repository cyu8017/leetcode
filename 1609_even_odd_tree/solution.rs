// LeetCode 1609 - Even Odd Tree
// https://leetcode.com/problems/even-odd-tree/

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
    pub fn is_even_odd_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let Some(root) = root else { return true };
        let mut q = vec![root];
        let mut level = 0i32;
        while !q.is_empty() {
            let mut prev = if level % 2 == 0 { i32::MIN } else { i32::MAX };
            let mut nxt = Vec::new();
            for node in q {
                let node = node.borrow();
                if node.val % 2 == level % 2 {
                    return false;
                }
                if level % 2 == 0 && node.val <= prev {
                    return false;
                }
                if level % 2 == 1 && node.val >= prev {
                    return false;
                }
                prev = node.val;
                if let Some(l) = node.left.clone() {
                    nxt.push(l);
                }
                if let Some(r) = node.right.clone() {
                    nxt.push(r);
                }
            }
            q = nxt;
            level += 1;
        }
        true
    }
}
