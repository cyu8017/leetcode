// LeetCode 0998 - Maximum Binary Tree II
// https://leetcode.com/problems/maximum-binary-tree-ii/

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
    pub fn insert_into_max_tree(
        root: Option<Rc<RefCell<TreeNode>>>,
        val: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        if root.is_none() || val > root.as_ref().unwrap().borrow().val {
            let node = Rc::new(RefCell::new(TreeNode::new(val)));
            node.borrow_mut().left = root;
            return Some(node);
        }
        let right = root.as_ref().unwrap().borrow_mut().right.take();
        root.as_ref().unwrap().borrow_mut().right = Self::insert_into_max_tree(right, val);
        root
    }
}
