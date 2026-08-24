struct Solution;

// LeetCode 2583 - Kth Largest Sum in a Binary Tree
// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

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
    pub fn kth_largest_level_sum(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i64 {
        let Some(root) = root else {
            return -1;
        };
        let mut sums = Vec::new();
        let mut q = VecDeque::new();
        q.push_back(root);
        while !q.is_empty() {
            let sz = q.len();
            let mut s = 0i64;
            for _ in 0..sz {
                let node = q.pop_front().unwrap();
                let n = node.borrow();
                s += n.val as i64;
                if let Some(left) = n.left.clone() {
                    q.push_back(left);
                }
                if let Some(right) = n.right.clone() {
                    q.push_back(right);
                }
            }
            sums.push(s);
        }
        sums.sort_by(|a, b| b.cmp(a));
        if k as usize > sums.len() {
            -1
        } else {
            sums[k as usize - 1]
        }
    }
}

fn main() {}
