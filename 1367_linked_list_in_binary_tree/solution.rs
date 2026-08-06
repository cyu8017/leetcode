// LeetCode 1367 - Linked List in Binary Tree
// https://leetcode.com/problems/linked-list-in-binary-tree/

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn is_sub_path(
        head: Option<Box<ListNode>>,
        root: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        fn match_path(head: &Option<Box<ListNode>>, root: &Option<Rc<RefCell<TreeNode>>>) -> bool {
            match head {
                None => true,
                Some(h) => match root {
                    None => false,
                    Some(r) => {
                        let n = r.borrow();
                        h.val == n.val
                            && (match_path(&h.next, &n.left) || match_path(&h.next, &n.right))
                    }
                },
            }
        }
        match root {
            None => false,
            Some(r) => {
                let n = r.borrow();
                match_path(&head, &Some(r.clone()))
                    || Self::is_sub_path(head.clone(), n.left.clone())
                    || Self::is_sub_path(head, n.right.clone())
            }
        }
    }
}
