// LeetCode 3157 - Find the Level of Tree with Minimum Sum
// https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

use std::cell::RefCell;
use std::collections::VecDeque;
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
    pub fn minimum_level(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let Some(root) = root else {
            return 0;
        };
        let mut q = VecDeque::new();
        q.push_back(root);
        let mut s = i64::MAX;
        let mut ans = 0;
        let mut level = 1;
        while !q.is_empty() {
            let m = q.len();
            let mut t = 0i64;
            for _ in 0..m {
                let node = q.pop_front().unwrap();
                let node = node.borrow();
                t += node.val as i64;
                if let Some(l) = node.left.clone() {
                    q.push_back(l);
                }
                if let Some(r) = node.right.clone() {
                    q.push_back(r);
                }
            }
            if s > t {
                s = t;
                ans = level;
            }
            level += 1;
        }
        ans
    }
}
