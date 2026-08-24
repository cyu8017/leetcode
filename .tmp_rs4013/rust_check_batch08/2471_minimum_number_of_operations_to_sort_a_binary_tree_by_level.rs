struct Solution;
// LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

use std::collections::{HashMap, VecDeque};
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
    pub fn minimum_operations(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let Some(root) = root else {
            return 0;
        };
        let mut ans = 0;
        let mut q = VecDeque::new();
        q.push_back(root);
        while !q.is_empty() {
            let sz = q.len();
            let mut vals = vec![0; sz];
            for i in 0..sz {
                let node = q.pop_front().unwrap();
                let n = node.borrow();
                vals[i] = n.val;
                if let Some(l) = &n.left {
                    q.push_back(l.clone());
                }
                if let Some(r) = &n.right {
                    q.push_back(r.clone());
                }
            }
            let mut sorted = vals.clone();
            sorted.sort_unstable();
            let mut pos: HashMap<i32, usize> = HashMap::new();
            for i in 0..sz {
                pos.insert(vals[i], i);
            }
            for i in 0..sz {
                if vals[i] != sorted[i] {
                    let j = pos[&sorted[i]];
                    vals.swap(i, j);
                    pos.insert(vals[j], j);
                    pos.insert(vals[i], i);
                    ans += 1;
                }
            }
        }
        ans
    }
}

fn main() {}
