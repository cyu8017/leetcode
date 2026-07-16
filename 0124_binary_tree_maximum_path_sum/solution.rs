// LeetCode 0124 - Binary Tree Maximum Path Sum
// https://leetcode.com/problems/binary-tree-maximum-path-sum/

use std::cell::RefCell;
use std::rc::Rc;
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode { pub val: i32, pub left: Option<Rc<RefCell<TreeNode>>>, pub right: Option<Rc<RefCell<TreeNode>>> }
impl TreeNode { #[inline] pub fn new(val: i32) -> Self { TreeNode { val, left: None, right: None } } }
impl Solution {
    fn gain(node: Option<Rc<RefCell<TreeNode>>>, best: &mut i32) -> i32 { match node { None => 0, Some(node) => { let node=node.borrow();let left=Self::gain(node.left.clone(),best).max(0);let right=Self::gain(node.right.clone(),best).max(0);*best=(*best).max(node.val+left+right);node.val+left.max(right) } } }
    pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 { let mut best=i32::MIN;Self::gain(root,&mut best);best }
}