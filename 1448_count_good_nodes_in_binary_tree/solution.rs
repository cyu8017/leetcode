// LeetCode 1448 - Count Good Nodes in Binary Tree
// https://leetcode.com/problems/count-good-nodes-in-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn good_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn visit(node: Option<Rc<RefCell<TreeNode>>>, maximum: i32) -> i32 {
            let Some(node) = node else { return 0 };
            let n = node.borrow();
            let good = i32::from(n.val >= maximum);
            let maximum = maximum.max(n.val);
            good + visit(n.left.clone(), maximum) + visit(n.right.clone(), maximum)
        }
        visit(root, i32::MIN)
    }
}
