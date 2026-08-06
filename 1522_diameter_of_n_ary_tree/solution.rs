// LeetCode 1522 - Diameter of N-Ary Tree
// https://leetcode.com/problems/diameter-of-n-ary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub children: Vec<Rc<RefCell<Node>>>,
}

impl Solution {
    pub fn diameter(root: Option<Rc<RefCell<Node>>>) -> i32 {
        let mut answer = 0;
        fn depth(node: &Rc<RefCell<Node>>, answer: &mut i32) -> i32 {
            let mut longest = 0;
            let mut second = 0;
            let children = node.borrow().children.clone();
            for child in children {
                let value = depth(&child, answer) + 1;
                if value > longest {
                    second = longest;
                    longest = value;
                } else if value > second {
                    second = value;
                }
            }
            *answer = (*answer).max(longest + second);
            longest
        }
        if let Some(root) = root {
            depth(&root, &mut answer);
        }
        answer
    }
}
