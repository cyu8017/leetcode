// LeetCode 3263 - Convert Doubly Linked List to Array I
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

use std::cell::RefCell;
use std::rc::Rc;

pub struct Node {
    pub val: i32,
    pub prev: Option<Rc<RefCell<Node>>>,
    pub next: Option<Rc<RefCell<Node>>>,
}

impl Node {
    pub fn new(val: i32) -> Self {
        Node {
            val,
            prev: None,
            next: None,
        }
    }
}

impl Solution {
    pub fn to_array(head: Option<Rc<RefCell<Node>>>) -> Vec<i32> {
        let mut ans = Vec::new();
        let mut cur = head;
        while let Some(node) = cur {
            ans.push(node.borrow().val);
            cur = node.borrow().next.clone();
        }
        ans
    }
}
