// LeetCode 0445 - Add Two Numbers II
// https://leetcode.com/problems/add-two-numbers-ii/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Rc<RefCell<ListNode>>>,
}

impl Solution {
    pub fn add_two_numbers(
        l1: Option<Rc<RefCell<ListNode>>>,
        l2: Option<Rc<RefCell<ListNode>>>,
    ) -> Option<Rc<RefCell<ListNode>>> {
        let mut stack1 = Vec::new();
        let mut stack2 = Vec::new();

        let mut current = l1;
        while let Some(node) = current {
            stack1.push(node.borrow().val);
            current = node.borrow().next.clone();
        }

        current = l2;
        while let Some(node) = current {
            stack2.push(node.borrow().val);
            current = node.borrow().next.clone();
        }

        let mut carry = 0;
        let mut head: Option<Rc<RefCell<ListNode>>> = None;
        while !stack1.is_empty() || !stack2.is_empty() || carry != 0 {
            let mut total = carry;
            if let Some(value) = stack1.pop() {
                total += value;
            }
            if let Some(value) = stack2.pop() {
                total += value;
            }
            carry = total / 10;
            head = Some(Rc::new(RefCell::new(ListNode {
                val: total % 10,
                next: head,
            })));
        }
        head
    }
}
