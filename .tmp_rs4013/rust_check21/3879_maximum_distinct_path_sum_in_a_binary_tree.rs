struct Solution;
// LeetCode 3879 - Maximum Distinct Path Sum in a Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn max_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut nodes = Vec::new();
        fn collect(node: Option<Rc<RefCell<TreeNode>>>, nodes: &mut Vec<Rc<RefCell<TreeNode>>>) {
            if let Some(n) = node {
                nodes.push(n.clone());
                let b = n.borrow();
                collect(b.left.clone(), nodes);
                collect(b.right.clone(), nodes);
            }
        }
        collect(root.clone(), &mut nodes);
        let idx: HashMap<usize, usize> = nodes
            .iter()
            .enumerate()
            .map(|(i, n)| (Rc::as_ptr(n) as usize, i))
            .collect();
        let mut g = vec![Vec::new(); nodes.len()];
        fn build(
            node: Option<Rc<RefCell<TreeNode>>>,
            parent: Option<usize>,
            idx: &HashMap<usize, usize>,
            g: &mut [Vec<Option<usize>>],
        ) {
            let Some(n) = node else {
                return;
            };
            let i = idx[&(Rc::as_ptr(&n) as usize)];
            let b = n.borrow();
            let left = b.left.as_ref().map(|c| idx[&(Rc::as_ptr(c) as usize)]);
            let right = b.right.as_ref().map(|c| idx[&(Rc::as_ptr(c) as usize)]);
            g[i] = vec![parent, left, right];
            build(b.left.clone(), Some(i), idx, g);
            build(b.right.clone(), Some(i), idx, g);
        }
        build(root, None, &idx, &mut g);
        fn dfs2(
            i: Option<usize>,
            nodes: &[Rc<RefCell<TreeNode>>],
            g: &[Vec<Option<usize>>],
            vis: &mut HashMap<i32, bool>,
        ) -> i32 {
            let Some(i) = i else {
                return 0;
            };
            let val = nodes[i].borrow().val;
            if *vis.get(&val).unwrap_or(&false) {
                return 0;
            }
            vis.insert(val, true);
            let mut best = 0;
            for &nxt in &g[i] {
                best = best.max(dfs2(nxt, nodes, g, vis));
            }
            vis.insert(val, false);
            val + best
        }
        let mut ans = i32::MIN;
        for i in 0..nodes.len() {
            let mut vis = HashMap::new();
            ans = ans.max(dfs2(Some(i), &nodes, &g, &mut vis));
        }
        ans
    }
}
