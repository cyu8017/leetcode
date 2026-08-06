// LeetCode 1379 - Find a Corresponding Node of a Binary Tree in a Clone of That Tree
// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn get_target_copy(
        original: Option<Rc<RefCell<TreeNode>>>,
        cloned: Option<Rc<RefCell<TreeNode>>>,
        target: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let wanted = target.as_ref().unwrap().borrow().val;
        let mut stack = vec![(original, cloned)];
        while let Some((a, b)) = stack.pop() {
            let (Some(a), Some(b)) = (a, b) else { continue };
            if a.borrow().val == wanted {
                return Some(b);
            }
            let (aa, bb) = (a.borrow(), b.borrow());
            if aa.left.is_some() {
                stack.push((aa.left.clone(), bb.left.clone()));
            }
            if aa.right.is_some() {
                stack.push((aa.right.clone(), bb.right.clone()));
            }
        }
        None
    }
}
