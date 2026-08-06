// LeetCode 1506 - Find Root of N-Ary Tree
// https://leetcode.com/problems/find-root-of-n-ary-tree/

use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub children: Vec<Rc<RefCell<Node>>>,
}

impl Solution {
    pub fn find_root(tree: Vec<Option<Rc<RefCell<Node>>>>) -> Option<Rc<RefCell<Node>>> {
        let mut value = 0;
        let mut nodes: HashMap<i32, Rc<RefCell<Node>>> = HashMap::new();
        for node in tree.into_iter().flatten() {
            let val = node.borrow().val;
            nodes.insert(val, node.clone());
            value ^= val;
            for child in &node.borrow().children {
                value ^= child.borrow().val;
            }
        }
        nodes.remove(&value)
    }
}
