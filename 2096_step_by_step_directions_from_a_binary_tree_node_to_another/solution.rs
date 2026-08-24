// LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    fn path(node: Option<Rc<RefCell<TreeNode>>>, target: i32, p: &mut String) -> bool {
        let Some(node) = node else {
            return false;
        };
        let node = node.borrow();
        if node.val == target {
            return true;
        }
        p.push('L');
        if Self::path(node.left.clone(), target, p) {
            return true;
        }
        p.pop();
        p.push('R');
        if Self::path(node.right.clone(), target, p) {
            return true;
        }
        p.pop();
        false
    }

    pub fn get_directions(
        root: Option<Rc<RefCell<TreeNode>>>,
        start_value: i32,
        dest_value: i32,
    ) -> String {
        let mut ps = String::new();
        let mut pd = String::new();
        Self::path(root.clone(), start_value, &mut ps);
        Self::path(root, dest_value, &mut pd);
        let mut i = 0;
        while i < ps.len() && i < pd.len() && ps.as_bytes()[i] == pd.as_bytes()[i] {
            i += 1;
        }
        "U".repeat(ps.len() - i) + &pd[i..]
    }
}
