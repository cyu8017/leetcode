// LeetCode 1382 - Balance a Binary Search Tree
// https://leetcode.com/problems/balance-a-binary-search-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn balance_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut nodes = Vec::new();
        fn walk(node: Option<Rc<RefCell<TreeNode>>>, nodes: &mut Vec<Rc<RefCell<TreeNode>>>) {
            if let Some(n) = node {
                let left = n.borrow().left.clone();
                let right = n.borrow().right.clone();
                walk(left, nodes);
                nodes.push(n);
                walk(right, nodes);
            }
        }
        walk(root, &mut nodes);
        fn build(nodes: &[Rc<RefCell<TreeNode>>], l: usize, r: usize) -> Option<Rc<RefCell<TreeNode>>> {
            if l >= r {
                return None;
            }
            let m = (l + r) / 2;
            let x = nodes[m].clone();
            {
                let mut n = x.borrow_mut();
                n.left = build(nodes, l, m);
                n.right = build(nodes, m + 1, r);
            }
            Some(x)
        }
        build(&nodes, 0, nodes.len())
    }
}
