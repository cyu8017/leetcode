// LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

use std::cell::RefCell;
use std::collections::{HashMap, HashSet, VecDeque};
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn amount_of_time(root: Option<Rc<RefCell<TreeNode>>>, start: i32) -> i32 {
        let mut g: HashMap<i32, Vec<i32>> = HashMap::new();
        fn build(
            node: &Option<Rc<RefCell<TreeNode>>>,
            parent: Option<i32>,
            g: &mut HashMap<i32, Vec<i32>>,
        ) {
            if let Some(n) = node {
                let n = n.borrow();
                if let Some(p) = parent {
                    g.entry(n.val).or_default().push(p);
                    g.entry(p).or_default().push(n.val);
                }
                build(&n.left, Some(n.val), g);
                build(&n.right, Some(n.val), g);
            }
        }
        build(&root, None, &mut g);
        let mut ans = 0;
        let mut vis = HashSet::new();
        vis.insert(start);
        let mut q = VecDeque::new();
        q.push_back((start, 0));
        while let Some((v, d)) = q.pop_front() {
            ans = ans.max(d);
            if let Some(neis) = g.get(&v) {
                for &nxt in neis {
                    if vis.insert(nxt) {
                        q.push_back((nxt, d + 1));
                    }
                }
            }
        }
        ans
    }
}
