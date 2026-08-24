// LeetCode 0590 - N-ary Tree Postorder Traversal
// https://leetcode.com/problems/n-ary-tree-postorder-traversal/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub children: Vec<Rc<RefCell<Node>>>,
}

impl Solution {
    fn dfs(node: Option<Rc<RefCell<Node>>>, result: &mut Vec<i32>) {
        let Some(node) = node else {
            return;
        };
        let node = node.borrow();
        for child in &node.children {
            Self::dfs(Some(child.clone()), result);
        }
        result.push(node.val);
    }

    pub fn postorder(root: Option<Rc<RefCell<Node>>>) -> Vec<i32> {
        let mut result = Vec::new();
        Self::dfs(root, &mut result);
        result
    }
}
