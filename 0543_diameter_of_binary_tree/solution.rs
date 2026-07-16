// LeetCode 0543 - Diameter of Binary Tree
// https://leetcode.com/problems/diameter-of-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut best = 0;

        fn depth(node: Option<Rc<RefCell<TreeNode>>>, best: &mut i32) -> i32 {
            let Some(node) = node else {
                return 0;
            };
            let left = depth(node.borrow().left.clone(), best);
            let right = depth(node.borrow().right.clone(), best);
            *best = (*best).max(left + right);
            1 + left.max(right)
        }

        depth(root, &mut best);
        best
    }
}
