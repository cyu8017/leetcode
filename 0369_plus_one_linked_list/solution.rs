// LeetCode 0369 - Plus One Linked List
// https://leetcode.com/problems/plus-one-linked-list/

use std::rc::Rc;
use std::cell::RefCell;

#[derive(Debug, PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Rc<RefCell<ListNode>>>,
}

impl ListNode {
    pub fn new(val: i32) -> Self {
        Self { val, next: None }
    }
}

impl Solution {
    pub fn plus_one(head: Option<Rc<RefCell<ListNode>>>) -> Option<Rc<RefCell<ListNode>>> {
        let sentinel = Rc::new(RefCell::new(ListNode {
            val: 0,
            next: head,
        }));
        let mut not_nine = sentinel.clone();
        let mut node = sentinel.borrow().next.clone();

        while let Some(current) = node {
            if current.borrow().val != 9 {
                not_nine = current.clone();
            }
            node = current.borrow().next.clone();
        }

        not_nine.borrow_mut().val += 1;
        let mut node = not_nine.borrow().next.clone();
        while let Some(current) = node {
            current.borrow_mut().val = 0;
            node = current.borrow().next.clone();
        }

        if sentinel.borrow().val == 1 {
            Some(sentinel)
        } else {
            sentinel.borrow().next.clone()
        }
    }
}
