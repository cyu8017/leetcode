// LeetCode 0235 - Lowest Common Ancestor of a Binary Search Tree
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn lowest_common_ancestor(
        root: Option<Rc<RefCell<TreeNode>>>,
        p: Rc<RefCell<TreeNode>>,
        q: Rc<RefCell<TreeNode>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let p_val = p.borrow().val;
        let q_val = q.borrow().val;
        let mut current = root;
        while let Some(node) = current.clone() {
            let val = node.borrow().val;
            if p_val < val && q_val < val {
                current = node.borrow().left.clone();
            } else if p_val > val && q_val > val {
                current = node.borrow().right.clone();
            } else {
                return Some(node);
            }
        }
        current
    }
}
