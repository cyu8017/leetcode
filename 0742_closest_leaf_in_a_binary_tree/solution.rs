// LeetCode 0742 - Closest Leaf in a Binary Tree
// https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

use std::cell::RefCell;
use std::collections::{HashMap, HashSet, VecDeque};
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
    pub fn find_closest_leaf(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut leaves = HashSet::new();
        Self::build(root, None, &mut graph, &mut leaves);
        let mut q = VecDeque::new();
        let mut seen = HashSet::new();
        seen.insert(k);
        q.push_back(k);
        while let Some(value) = q.pop_front() {
            if leaves.contains(&value) {
                return value;
            }
            if let Some(neighbors) = graph.get(&value) {
                for &neighbor in neighbors {
                    if seen.insert(neighbor) {
                        q.push_back(neighbor);
                    }
                }
            }
        }
        -1
    }

    fn build(
        node: Option<Rc<RefCell<TreeNode>>>,
        parent: Option<i32>,
        graph: &mut HashMap<i32, Vec<i32>>,
        leaves: &mut HashSet<i32>,
    ) {
        let Some(node) = node else {
            return;
        };
        let node = node.borrow();
        if let Some(p) = parent {
            graph.entry(node.val).or_default().push(p);
            graph.entry(p).or_default().push(node.val);
        }
        if node.left.is_none() && node.right.is_none() {
            leaves.insert(node.val);
        }
        Self::build(node.right.clone(), Some(node.val), graph, leaves);
        Self::build(node.left.clone(), Some(node.val), graph, leaves);
    }
}
