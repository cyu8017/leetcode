// LeetCode 0863 - All Nodes Distance K in Binary Tree
// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

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
    pub fn distance_k(
        root: Option<Rc<RefCell<TreeNode>>>,
        target: Option<Rc<RefCell<TreeNode>>>,
        k: i32,
    ) -> Vec<i32> {
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        Self::build(root, None, &mut graph);
        let target_val = target.map(|t| t.borrow().val).unwrap_or(0);
        let mut queue = VecDeque::from([(target_val, 0)]);
        let mut seen = HashSet::from([target_val]);
        let mut ans = Vec::new();
        while let Some((node, dist)) = queue.pop_front() {
            if dist == k {
                ans.push(node);
                continue;
            }
            if let Some(neis) = graph.get(&node) {
                for &nei in neis {
                    if seen.insert(nei) {
                        queue.push_back((nei, dist + 1));
                    }
                }
            }
        }
        ans
    }

    fn build(
        node: Option<Rc<RefCell<TreeNode>>>,
        parent: Option<i32>,
        graph: &mut HashMap<i32, Vec<i32>>,
    ) {
        if let Some(node) = node {
            let node = node.borrow();
            if let Some(p) = parent {
                graph.entry(node.val).or_default().push(p);
                graph.entry(p).or_default().push(node.val);
            }
            Self::build(node.left.clone(), Some(node.val), graph);
            Self::build(node.right.clone(), Some(node.val), graph);
        }
    }
}
