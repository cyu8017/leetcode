// LeetCode 1612 - Check If Two Expression Trees are Equivalent
// https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: char,
    pub left: Option<Rc<RefCell<Node>>>,
    pub right: Option<Rc<RefCell<Node>>>,
}

impl Node {
    #[inline]
    pub fn new(val: char) -> Self {
        Node { val, left: None, right: None }
    }
}

impl Solution {
    pub fn check_equivalence(
        root1: Option<Rc<RefCell<Node>>>,
        root2: Option<Rc<RefCell<Node>>>,
    ) -> bool {
        let mut a = [0i32; 26];
        let mut b = [0i32; 26];
        Self::count(&root1, &mut a);
        Self::count(&root2, &mut b);
        a == b
    }

    fn count(node: &Option<Rc<RefCell<Node>>>, out: &mut [i32; 26]) {
        let Some(node) = node else { return };
        let node = node.borrow();
        if node.val == '+' {
            Self::count(&node.left, out);
            Self::count(&node.right, out);
        } else {
            out[(node.val as u8 - b'a') as usize] += 1;
        }
    }
}
