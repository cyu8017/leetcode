// LeetCode 1038 - Binary Search Tree to Greater Sum Tree
// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

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
    pub fn bst_to_gst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        fn reverse_inorder(node: &Option<Rc<RefCell<TreeNode>>>, total: &mut i32) {
            if let Some(rc) = node {
                let (left, right) = {
                    let n = rc.borrow();
                    (n.left.clone(), n.right.clone())
                };
                reverse_inorder(&right, total);
                {
                    let mut n = rc.borrow_mut();
                    *total += n.val;
                    n.val = *total;
                }
                reverse_inorder(&left, total);
            }
        }
        let mut total = 0;
        reverse_inorder(&root, &mut total);
        root
    }
}
