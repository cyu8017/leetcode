// LeetCode 0589 - N-ary Tree Preorder Traversal
// https://leetcode.com/problems/n-ary-tree-preorder-traversal/

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
        result.push(node.val);
        for child in &node.children {
            Self::dfs(Some(child.clone()), result);
        }
    }

    pub fn preorder(root: Option<Rc<RefCell<Node>>>) -> Vec<i32> {
        let mut result = Vec::new();
        Self::dfs(root, &mut result);
        result
    }
}
