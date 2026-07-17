// LeetCode 1740 - Find Distance in a Binary Tree
// https://leetcode.com/problems/find-distance-in-a-binary-tree/

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
    pub fn find_distance(root: Option<Rc<RefCell<TreeNode>>>, p: i32, q: i32) -> i32 {
        fn dfs(
            node: &Option<Rc<RefCell<TreeNode>>>,
            parent: Option<i32>,
            graph: &mut HashMap<i32, Vec<i32>>,
        ) {
            if let Some(rc) = node {
                let borrowed = rc.borrow();
                graph.entry(borrowed.val).or_default();
                if let Some(parent_val) = parent {
                    graph.entry(borrowed.val).or_default().push(parent_val);
                    graph.entry(parent_val).or_default().push(borrowed.val);
                }
                dfs(&borrowed.left, Some(borrowed.val), graph);
                dfs(&borrowed.right, Some(borrowed.val), graph);
            }
        }

        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        dfs(&root, None, &mut graph);
        let mut queue = VecDeque::new();
        queue.push_back((p, 0));
        let mut seen = HashSet::new();
        seen.insert(p);
        while let Some((node, dist)) = queue.pop_front() {
            if node == q {
                return dist;
            }
            if let Some(neighbors) = graph.get(&node) {
                for &nei in neighbors {
                    if seen.insert(nei) {
                        queue.push_back((nei, dist + 1));
                    }
                }
            }
        }
        -1
    }
}
