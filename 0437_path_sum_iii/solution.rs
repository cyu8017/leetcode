// LeetCode 0437 - Path Sum III
// https://leetcode.com/problems/path-sum-iii/

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
    fn dfs(
        node: Option<Rc<RefCell<TreeNode>>>,
        current: i64,
        target_sum: i32,
        prefix_counts: &mut HashMap<i64, i32>,
    ) -> i32 {
        let Some(node) = node else {
            return 0;
        };

        let node = node.borrow();
        let current = current + i64::from(node.val);
        let mut total = *prefix_counts.get(&(current - i64::from(target_sum))).unwrap_or(&0);
        *prefix_counts.entry(current).or_insert(0) += 1;

        total += Self::dfs(node.left.clone(), current, target_sum, prefix_counts);
        total += Self::dfs(node.right.clone(), current, target_sum, prefix_counts);

        if let Some(count) = prefix_counts.get_mut(&current) {
            *count -= 1;
        }
        total
    }

    pub fn path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> i32 {
        let mut prefix_counts = HashMap::new();
        prefix_counts.insert(0, 1);
        Self::dfs(root, 0, target_sum, &mut prefix_counts)
    }
}
