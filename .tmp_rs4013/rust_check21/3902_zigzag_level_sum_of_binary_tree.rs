struct Solution;
// LeetCode 3902 - Zigzag Level Sum of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn zigzag_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i64> {
        let Some(root) = root else {
            return Vec::new();
        };
        let mut ans = Vec::new();
        let mut q = vec![root];
        let mut left = true;
        while !q.is_empty() {
            let mut nq = Vec::new();
            for node in &q {
                let b = node.borrow();
                if let Some(l) = b.left.clone() {
                    nq.push(l);
                }
                if let Some(r) = b.right.clone() {
                    nq.push(r);
                }
            }
            let m = q.len();
            let mut s = 0i64;
            for i in 0..m {
                let node = if left { &q[i] } else { &q[m - i - 1] };
                let b = node.borrow();
                let child = if left { b.left.clone() } else { b.right.clone() };
                if child.is_none() {
                    break;
                }
                s += b.val as i64;
            }
            ans.push(s);
            left = !left;
            q = nq;
        }
        ans
    }
}
