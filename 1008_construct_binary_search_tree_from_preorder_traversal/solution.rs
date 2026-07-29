// LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal
// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

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
    pub fn bst_from_preorder(preorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        fn build(preorder: &[i32], i: &mut usize, bound: i32) -> Option<Rc<RefCell<TreeNode>>> {
            if *i == preorder.len() || preorder[*i] > bound {
                return None;
            }
            let val = preorder[*i];
            *i += 1;
            let node = Rc::new(RefCell::new(TreeNode::new(val)));
            node.borrow_mut().left = build(preorder, i, val);
            node.borrow_mut().right = build(preorder, i, bound);
            Some(node)
        }
        let mut i = 0;
        build(&preorder, &mut i, i32::MAX)
    }
}
