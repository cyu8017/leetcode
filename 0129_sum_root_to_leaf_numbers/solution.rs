// LeetCode 0129 - Sum Root to Leaf Numbers
// https://leetcode.com/problems/sum-root-to-leaf-numbers/

use std::cell::RefCell;
use std::rc::Rc;
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode { pub val: i32, pub left: Option<Rc<RefCell<TreeNode>>>, pub right: Option<Rc<RefCell<TreeNode>>> }
impl TreeNode { #[inline] pub fn new(val: i32) -> Self { TreeNode { val, left: None, right: None } } }
impl Solution {
    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, value: i32) -> i32 { match node { None => 0, Some(node) => { let node=node.borrow();let value=value*10+node.val;if node.left.is_none()&&node.right.is_none(){value}else{Self::dfs(node.left.clone(),value)+Self::dfs(node.right.clone(),value)} } } }
    pub fn sum_numbers(root: Option<Rc<RefCell<TreeNode>>>) -> i32 { Self::dfs(root,0) }
}