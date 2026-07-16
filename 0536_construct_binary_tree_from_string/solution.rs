// LeetCode 0536 - Construct Binary Tree from String
// https://leetcode.com/problems/construct-binary-tree-from-string/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

impl Solution {
    pub fn str2tree(s: String) -> Option<Rc<RefCell<TreeNode>>> {
        if s.is_empty() {
            return None;
        }

        let bytes = s.as_bytes();
        let mut index = 0;

        fn parse(
            bytes: &[u8],
            index: &mut usize,
        ) -> Option<Rc<RefCell<TreeNode>>> {
            if *index >= bytes.len() {
                return None;
            }

            let mut sign = 1;
            if bytes[*index] == b'-' {
                sign = -1;
                *index += 1;
            }

            let mut value = 0;
            while *index < bytes.len() && bytes[*index].is_ascii_digit() {
                value = value * 10 + (bytes[*index] - b'0') as i32;
                *index += 1;
            }

            let node = Rc::new(RefCell::new(TreeNode::new(sign * value)));

            if *index < bytes.len() && bytes[*index] == b'(' {
                *index += 1;
                node.borrow_mut().left = parse(bytes, index);
                *index += 1;
            }

            if *index < bytes.len() && bytes[*index] == b'(' {
                *index += 1;
                node.borrow_mut().right = parse(bytes, index);
                *index += 1;
            }

            Some(node)
        }

        parse(bytes, &mut index)
    }
}
