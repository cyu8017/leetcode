// LeetCode 0971 - Flip Binary Tree To Match Preorder Traversal
// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

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
    pub fn flip_match_voyage(
        root: Option<Rc<RefCell<TreeNode>>>,
        voyage: Vec<i32>,
    ) -> Vec<i32> {
        fn dfs(
            node: Option<Rc<RefCell<TreeNode>>>,
            voyage: &[i32],
            i: &mut usize,
            ans: &mut Vec<i32>,
        ) -> bool {
            let Some(node) = node else {
                return true;
            };
            let node = node.borrow();
            if node.val != voyage[*i] {
                return false;
            }
            *i += 1;
            if let Some(left) = &node.left {
                if *i < voyage.len() && left.borrow().val != voyage[*i] {
                    ans.push(node.val);
                    return dfs(node.right.clone(), voyage, i, ans)
                        && dfs(node.left.clone(), voyage, i, ans);
                }
            }
            dfs(node.left.clone(), voyage, i, ans) && dfs(node.right.clone(), voyage, i, ans)
        }
        let mut i = 0;
        let mut ans = Vec::new();
        if dfs(root, &voyage, &mut i, &mut ans) {
            ans
        } else {
            vec![-1]
        }
    }
}
