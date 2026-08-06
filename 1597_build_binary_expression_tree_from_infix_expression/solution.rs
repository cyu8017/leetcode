// LeetCode 1597 - Build Binary Expression Tree From Infix Expression
// https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: String,
    pub left: Option<Rc<RefCell<Node>>>,
    pub right: Option<Rc<RefCell<Node>>>,
}

impl Node {
    pub fn new(val: String) -> Self {
        Self {
            val,
            left: None,
            right: None,
        }
    }
}

impl Solution {
    pub fn exp_tree(s: String) -> Option<Rc<RefCell<Node>>> {
        let mut nodes: Vec<Rc<RefCell<Node>>> = Vec::new();
        let mut ops: Vec<char> = Vec::new();
        let priority = |c: char| match c {
            '+' | '-' => 1,
            '*' | '/' => 2,
            _ => 0,
        };
        let apply = |nodes: &mut Vec<Rc<RefCell<Node>>>, ops: &mut Vec<char>| {
            let op = ops.pop().unwrap();
            let right = nodes.pop().unwrap();
            let left = nodes.pop().unwrap();
            let node = Rc::new(RefCell::new(Node::new(op.to_string())));
            node.borrow_mut().left = Some(left);
            node.borrow_mut().right = Some(right);
            nodes.push(node);
        };
        for ch in s.chars() {
            if ch.is_ascii_digit() {
                nodes.push(Rc::new(RefCell::new(Node::new(ch.to_string()))));
            } else if ch == '(' {
                ops.push(ch);
            } else if ch == ')' {
                while *ops.last().unwrap() != '(' {
                    apply(&mut nodes, &mut ops);
                }
                ops.pop();
            } else {
                while ops
                    .last()
                    .map_or(false, |&op| op != '(' && priority(op) >= priority(ch))
                {
                    apply(&mut nodes, &mut ops);
                }
                ops.push(ch);
            }
        }
        while !ops.is_empty() {
            apply(&mut nodes, &mut ops);
        }
        nodes.pop()
    }
}
