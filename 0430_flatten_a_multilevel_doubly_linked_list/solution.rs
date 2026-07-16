// LeetCode 0430 - Flatten a Multilevel Doubly Linked List
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub prev: Option<Rc<RefCell<Node>>>,
    pub next: Option<Rc<RefCell<Node>>>,
    pub child: Option<Rc<RefCell<Node>>>,
}

impl Solution {
    pub fn flatten(head: Option<Rc<RefCell<Node>>>) -> Option<Rc<RefCell<Node>>> {
        let mut current = head.clone();

        while let Some(current_node) = current.clone() {
            let child = current_node.borrow().child.clone();
            if let Some(child_head) = child {
                let next_node = current_node.borrow().next.clone();
                let flattened_child = Self::flatten(Some(child_head.clone()));

                if let Some(flattened_child) = flattened_child {
                    current_node.borrow_mut().next = Some(flattened_child.clone());
                    flattened_child.borrow_mut().prev = Some(current_node.clone());

                    let mut tail = flattened_child.clone();
                    loop {
                        let next = tail.borrow().next.clone();
                        if let Some(next) = next {
                            tail = next;
                        } else {
                            break;
                        }
                    }

                    tail.borrow_mut().next = next_node.clone();
                    if let Some(next_node) = next_node {
                        next_node.borrow_mut().prev = Some(tail);
                    }
                }

                current_node.borrow_mut().child = None;
            }

            current = current_node.borrow().next.clone();
        }

        head
    }
}
