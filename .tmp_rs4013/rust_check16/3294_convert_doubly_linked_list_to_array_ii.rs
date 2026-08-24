struct Solution;
// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

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
    pub fn to_array(node: Option<Rc<RefCell<Node>>>) -> Vec<i32> {
        let mut cur = node;
        while let Some(n) = cur.clone() {
            let prev = n.borrow().prev.clone();
            if prev.is_none() {
                break;
            }
            cur = prev;
        }
        let mut ans = Vec::new();
        while let Some(n) = cur {
            ans.push(n.borrow().val);
            cur = n.borrow().next.clone();
        }
        ans
    }
}

fn main() {}
