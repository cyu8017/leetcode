// LeetCode 1628 - Design an Expression Tree With Evaluate Function
// https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

use std::cell::RefCell;
use std::rc::Rc;

pub struct Node {
    pub val: String,
    pub left: Option<Rc<RefCell<Node>>>,
    pub right: Option<Rc<RefCell<Node>>>,
}

impl Node {
    pub fn new(val: String) -> Self {
        Self { val, left: None, right: None }
    }

    pub fn evaluate(&self) -> i32 {
        match self.val.as_str() {
            "+" | "-" | "*" | "/" => {
                let a = self.left.as_ref().unwrap().borrow().evaluate();
                let b = self.right.as_ref().unwrap().borrow().evaluate();
                match self.val.as_str() {
                    "+" => a + b,
                    "-" => a - b,
                    "*" => a * b,
                    _ => a / b,
                }
            }
            _ => self.val.parse().unwrap_or(0),
        }
    }
}

pub struct TreeBuilder;

impl TreeBuilder {
    pub fn new() -> Self {
        Self
    }

    pub fn exp_tree(&self, postfix: Vec<String>) -> Option<Rc<RefCell<Node>>> {
        let mut stack: Vec<Rc<RefCell<Node>>> = Vec::new();
        for token in postfix {
            let is_op = matches!(token.as_str(), "+" | "-" | "*" | "/");
            let node = Rc::new(RefCell::new(Node::new(token)));
            if is_op {
                let right = stack.pop().unwrap();
                let left = stack.pop().unwrap();
                node.borrow_mut().right = Some(right);
                node.borrow_mut().left = Some(left);
            }
            stack.push(node);
        }
        stack.pop()
    }
}
