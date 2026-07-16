// LeetCode 0426 - Convert Binary Search Tree to Sorted Doubly Linked List
// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn tree_to_doubly_list(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let Some(root) = root else {
            return None;
        };

        let first: Rc<RefCell<Option<Rc<RefCell<TreeNode>>>>> = Rc::new(RefCell::new(None));
        let last: Rc<RefCell<Option<Rc<RefCell<TreeNode>>>>> = Rc::new(RefCell::new(None));

        fn inorder(
            node: Option<Rc<RefCell<TreeNode>>>,
            first: &Rc<RefCell<Option<Rc<RefCell<TreeNode>>>>>,
            last: &Rc<RefCell<Option<Rc<RefCell<TreeNode>>>>>,
        ) {
            let Some(node) = node else {
                return;
            };

            inorder(node.borrow().left.clone(), first, last);

            let mut node_ref = node.borrow_mut();
            if let Some(last_node) = last.borrow().clone() {
                last_node.borrow_mut().right = Some(node.clone());
                node_ref.left = Some(last_node);
            } else {
                *first.borrow_mut() = Some(node.clone());
            }
            *last.borrow_mut() = Some(node.clone());

            let right = node_ref.right.clone();
            drop(node_ref);
            inorder(right, first, last);
        }

        inorder(Some(root), &first, &last);

        if let (Some(first_node), Some(last_node)) =
            (first.borrow().clone(), last.borrow().clone())
        {
            first_node.borrow_mut().left = Some(last_node.clone());
            last_node.borrow_mut().right = Some(first_node.clone());
            Some(first_node)
        } else {
            None
        }
    }
}
