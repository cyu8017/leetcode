// LeetCode 0508 - Most Frequent Subtree Sum
// https://leetcode.com/problems/most-frequent-subtree-sum/

use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    fn subtree_sum(node: Option<Rc<RefCell<TreeNode>>>, counts: &mut HashMap<i32, i32>) -> i32 {
        let Some(node) = node else {
            return 0;
        };
        let node = node.borrow();
        let total = node.val
            + Self::subtree_sum(node.left.clone(), counts)
            + Self::subtree_sum(node.right.clone(), counts);
        *counts.entry(total).or_insert(0) += 1;
        total
    }

    pub fn find_frequent_tree_sum(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut counts = HashMap::new();
        Self::subtree_sum(root, &mut counts);
        if counts.is_empty() {
            return Vec::new();
        }
        let best = *counts.values().max().unwrap();
        let mut result: Vec<i32> = counts
            .into_iter()
            .filter(|(_, count)| *count == best)
            .map(|(value, _)| value)
            .collect();
        result.sort_unstable();
        result
    }
}
