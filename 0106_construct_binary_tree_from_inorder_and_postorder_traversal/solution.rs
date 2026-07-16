// LeetCode 0106 - Construct Binary Tree from Inorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

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
    pub fn build_tree(inorder: Vec<i32>, postorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut index = HashMap::new();
        for (i, &v) in inorder.iter().enumerate() {
            index.insert(v, i as i32);
        }
        let mut post_index = postorder.len() as i32 - 1;
        Self::build(&postorder, &index, &mut post_index, 0, inorder.len() as i32 - 1)
    }

    fn build(
        postorder: &[i32],
        index: &HashMap<i32, i32>,
        post_index: &mut i32,
        left: i32,
        right: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        if left > right {
            return None;
        }
        let root_val = postorder[*post_index as usize];
        *post_index -= 1;
        let mid = index[&root_val];
        let mut root = TreeNode::new(root_val);
        root.right = Self::build(postorder, index, post_index, mid + 1, right);
        root.left = Self::build(postorder, index, post_index, left, mid - 1);
        Some(Rc::new(RefCell::new(root)))
    }
}