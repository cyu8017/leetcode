// LeetCode 1485 - Clone Binary Tree With Random Pointer
// https://leetcode.com/problems/clone-binary-tree-with-random-pointer/

use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub left: Option<Rc<RefCell<Node>>>,
    pub right: Option<Rc<RefCell<Node>>>,
    pub random: Option<Rc<RefCell<Node>>>,
}

impl Solution {
    pub fn copy_random_binary_tree(
        root: Option<Rc<RefCell<Node>>>,
    ) -> Option<Rc<RefCell<Node>>> {
        let mut copies: HashMap<*const RefCell<Node>, Rc<RefCell<Node>>> = HashMap::new();
        fn clone_node(
            node: Option<Rc<RefCell<Node>>>,
            copies: &mut HashMap<*const RefCell<Node>, Rc<RefCell<Node>>>,
        ) -> Option<Rc<RefCell<Node>>> {
            let node = node?;
            let key = Rc::as_ptr(&node);
            if let Some(c) = copies.get(&key) {
                return Some(c.clone());
            }
            let val = node.borrow().val;
            let copy = Rc::new(RefCell::new(Node {
                val,
                left: None,
                right: None,
                random: None,
            }));
            copies.insert(key, copy.clone());
            let (left, right, random) = {
                let n = node.borrow();
                (n.left.clone(), n.right.clone(), n.random.clone())
            };
            copy.borrow_mut().left = clone_node(left, copies);
            copy.borrow_mut().right = clone_node(right, copies);
            copy.borrow_mut().random = clone_node(random, copies);
            Some(copy)
        }
        clone_node(root, &mut copies)
    }
}
