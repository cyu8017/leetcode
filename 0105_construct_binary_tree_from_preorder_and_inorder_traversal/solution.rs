// LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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
    pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut index = HashMap::new();
        for (i, &v) in inorder.iter().enumerate() {
            index.insert(v, i as i32);
        }
        let mut pre_index = 0;
        Self::build(&preorder, &index, &mut pre_index, 0, inorder.len() as i32 - 1)
    }

    fn build(
        preorder: &[i32],
        index: &HashMap<i32, i32>,
        pre_index: &mut usize,
        left: i32,
        right: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        if left > right {
            return None;
        }
        let root_val = preorder[*pre_index];
        *pre_index += 1;
        let mid = index[&root_val];
        let mut root = TreeNode::new(root_val);
        root.left = Self::build(preorder, index, pre_index, left, mid - 1);
        root.right = Self::build(preorder, index, pre_index, mid + 1, right);
        Some(Rc::new(RefCell::new(root)))
    }
}