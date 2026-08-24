struct Solution;
// LeetCode 0652 - Find Duplicate Subtrees
// https://leetcode.com/problems/find-duplicate-subtrees/

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
use std::collections::HashMap;

impl Solution {
    fn serialize(
        node: &Option<Rc<RefCell<TreeNode>>>,
        counts: &mut HashMap<String, i32>,
        result: &mut Vec<Option<Rc<RefCell<TreeNode>>>>,
    ) -> String {
        let Some(node_rc) = node else {
            return "#".to_string();
        };
        let node = node_rc.borrow();
        let key = format!(
            "{},{},{}",
            node.val,
            Self::serialize(&node.left, counts, result),
            Self::serialize(&node.right, counts, result)
        );
        let count = counts.entry(key.clone()).or_insert(0);
        *count += 1;
        if *count == 2 {
            result.push(Some(node_rc.clone()));
        }
        key
    }

    pub fn find_duplicate_subtrees(
        root: Option<Rc<RefCell<TreeNode>>>,
    ) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        let mut counts = HashMap::new();
        let mut result = Vec::new();
        Self::serialize(&root, &mut counts, &mut result);
        result
    }
}

fn main() {}
