// LeetCode 0501 - Find Mode in Binary Search Tree
// https://leetcode.com/problems/find-mode-in-binary-search-tree/

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
    fn inorder(node: Option<Rc<RefCell<TreeNode>>>, counts: &mut HashMap<i32, i32>, best: &mut i32) {
        let Some(node) = node else {
            return;
        };
        let node = node.borrow();
        Self::inorder(node.left.clone(), counts, best);
        let count = counts.entry(node.val).or_insert(0);
        *count += 1;
        *best = (*best).max(*count);
        Self::inorder(node.right.clone(), counts, best);
    }

    pub fn find_mode(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut counts = HashMap::new();
        let mut best = 0;
        Self::inorder(root, &mut counts, &mut best);
        counts
            .into_iter()
            .filter(|(_, count)| *count == best)
            .map(|(value, _)| value)
            .collect()
    }
}
