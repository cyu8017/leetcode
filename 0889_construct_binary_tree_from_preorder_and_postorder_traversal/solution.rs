// LeetCode 0889 - Construct Binary Tree from Preorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

use std::cell::RefCell;
use std::collections::HashMap;
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
    pub fn construct_from_pre_post(
        preorder: Vec<i32>,
        postorder: Vec<i32>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let mut post_index = HashMap::new();
        for (i, &v) in postorder.iter().enumerate() {
            post_index.insert(v, i as i32);
        }
        fn build(
            preorder: &[i32],
            post_index: &HashMap<i32, i32>,
            pre_lo: i32,
            pre_hi: i32,
            post_lo: i32,
            post_hi: i32,
        ) -> Option<Rc<RefCell<TreeNode>>> {
            if pre_lo > pre_hi {
                return None;
            }
            let root = Rc::new(RefCell::new(TreeNode::new(preorder[pre_lo as usize])));
            if pre_lo == pre_hi {
                return Some(root);
            }
            let left_val = preorder[(pre_lo + 1) as usize];
            let left_post = post_index[&left_val];
            let left_size = left_post - post_lo + 1;
            root.borrow_mut().left = build(
                preorder,
                post_index,
                pre_lo + 1,
                pre_lo + left_size,
                post_lo,
                left_post,
            );
            root.borrow_mut().right = build(
                preorder,
                post_index,
                pre_lo + left_size + 1,
                pre_hi,
                left_post + 1,
                post_hi - 1,
            );
            Some(root)
        }
        let n = preorder.len() as i32;
        build(&preorder, &post_index, 0, n - 1, 0, n - 1)
    }
}
