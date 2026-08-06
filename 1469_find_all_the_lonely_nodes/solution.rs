// LeetCode 1469 - Find All The Lonely Nodes
// https://leetcode.com/problems/find-all-the-lonely-nodes/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn get_lonely_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut ans = Vec::new();
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, ans: &mut Vec<i32>) {
            let Some(node) = node else { return };
            let n = node.borrow();
            match (&n.left, &n.right) {
                (Some(child), None) | (None, Some(child)) => ans.push(child.borrow().val),
                _ => {}
            }
            dfs(n.left.clone(), ans);
            dfs(n.right.clone(), ans);
        }
        dfs(root, &mut ans);
        ans
    }
}
