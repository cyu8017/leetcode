// LeetCode 2196 - Create Binary Tree From Descriptions
// https://leetcode.com/problems/create-binary-tree-from-descriptions/

use std::collections::{HashMap, HashSet};
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
    pub fn create_binary_tree(descriptions: Vec<Vec<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut nodes: HashMap<i32, Rc<RefCell<TreeNode>>> = HashMap::new();
        let mut child = HashSet::new();
        for d in descriptions {
            let (p, c, is_left) = (d[0], d[1], d[2]);
            nodes.entry(p).or_insert_with(|| Rc::new(RefCell::new(TreeNode::new(p))));
            nodes.entry(c).or_insert_with(|| Rc::new(RefCell::new(TreeNode::new(c))));
            let parent = nodes.get(&p).unwrap().clone();
            let ch = nodes.get(&c).unwrap().clone();
            if is_left == 1 {
                parent.borrow_mut().left = Some(ch);
            } else {
                parent.borrow_mut().right = Some(ch);
            }
            child.insert(c);
        }
        for (v, node) in nodes {
            if !child.contains(&v) {
                return Some(node);
            }
        }
        None
    }
}
