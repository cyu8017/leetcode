// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

use std::collections::VecDeque;
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
    pub fn replace_value_in_tree(
        root: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let root = root?;
        root.borrow_mut().val = 0;
        let mut q = VecDeque::new();
        q.push_back(root.clone());
        while !q.is_empty() {
            let sz = q.len();
            let mut level_sum = 0;
            let mut level = Vec::new();
            for _ in 0..sz {
                let node = q.pop_front().unwrap();
                {
                    let b = node.borrow();
                    if let Some(l) = &b.left {
                        level_sum += l.borrow().val;
                    }
                    if let Some(r) = &b.right {
                        level_sum += r.borrow().val;
                    }
                }
                level.push(node);
            }
            for node in level {
                let (left, right) = {
                    let b = node.borrow();
                    (b.left.clone(), b.right.clone())
                };
                let mut cousin = level_sum;
                if let Some(ref l) = left {
                    cousin -= l.borrow().val;
                }
                if let Some(ref r) = right {
                    cousin -= r.borrow().val;
                }
                if let Some(l) = left {
                    l.borrow_mut().val = cousin;
                    q.push_back(l);
                }
                if let Some(r) = right {
                    r.borrow_mut().val = cousin;
                    q.push_back(r);
                }
            }
        }
        Some(root)
    }
}
