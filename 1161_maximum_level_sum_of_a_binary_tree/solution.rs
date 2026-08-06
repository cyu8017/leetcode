// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

impl Solution {
    pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let root = root.unwrap();
        let mut queue = VecDeque::new();
        queue.push_back(root.clone());
        let mut best_sum = root.borrow().val;
        let mut best_level = 1;
        let mut level = 1;
        while !queue.is_empty() {
            let size = queue.len();
            let mut sum = 0;
            for _ in 0..size {
                let node = queue.pop_front().unwrap();
                let b = node.borrow();
                sum += b.val;
                if let Some(l) = b.left.clone() {
                    queue.push_back(l);
                }
                if let Some(r) = b.right.clone() {
                    queue.push_back(r);
                }
            }
            if sum > best_sum {
                best_sum = sum;
                best_level = level;
            }
            level += 1;
        }
        best_level
    }
}
