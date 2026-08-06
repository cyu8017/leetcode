// LeetCode 1305 - All Elements in Two Binary Search Trees
// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

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
        TreeNode { val, left: None, right: None }
    }
}

impl Solution {
    pub fn get_all_elements(
        root1: Option<Rc<RefCell<TreeNode>>>,
        root2: Option<Rc<RefCell<TreeNode>>>,
    ) -> Vec<i32> {
        fn inorder(root: Option<Rc<RefCell<TreeNode>>>, out: &mut Vec<i32>) {
            if let Some(node) = root {
                let n = node.borrow();
                inorder(n.left.clone(), out);
                out.push(n.val);
                inorder(n.right.clone(), out);
            }
        }
        let mut a = Vec::new();
        let mut b = Vec::new();
        inorder(root1, &mut a);
        inorder(root2, &mut b);
        let mut answer = Vec::with_capacity(a.len() + b.len());
        let (mut i, mut j) = (0, 0);
        while i < a.len() || j < b.len() {
            if j == b.len() || (i < a.len() && a[i] <= b[j]) {
                answer.push(a[i]);
                i += 1;
            } else {
                answer.push(b[j]);
                j += 1;
            }
        }
        answer
    }
}
