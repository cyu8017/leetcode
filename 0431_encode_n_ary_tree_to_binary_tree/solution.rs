// LeetCode 0431 - Encode N-ary Tree to Binary Tree
// https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub children: Vec<Rc<RefCell<Node>>>,
}

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn encode_nary_tree(root: Option<Rc<RefCell<Node>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let Some(root) = root else {
            return None;
        };

        let root = root.borrow();
        let binary = Rc::new(RefCell::new(TreeNode {
            val: root.val,
            left: None,
            right: None,
        }));

        if root.children.is_empty() {
            return Some(binary);
        }

        binary.borrow_mut().left = Self::encode_nary_tree(Some(root.children[0].clone()));
        let mut sibling = binary.borrow().left.clone();
        for child in root.children.iter().skip(1) {
            let encoded = Self::encode_nary_tree(Some(child.clone()));
            if let Some(ref mut current) = sibling {
                current.borrow_mut().right = encoded.clone();
                sibling = encoded;
            }
        }

        Some(binary)
    }

    pub fn decode_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<Node>>> {
        let Some(root) = root else {
            return None;
        };

        let root = root.borrow();
        let node = Rc::new(RefCell::new(Node {
            val: root.val,
            children: Vec::new(),
        }));

        let mut current = root.left.clone();
        while let Some(next) = current {
            node.borrow_mut()
                .children
                .push(Self::decode_binary_tree(Some(next.clone())).unwrap());
            current = next.borrow().right.clone();
        }

        Some(node)
    }
}
