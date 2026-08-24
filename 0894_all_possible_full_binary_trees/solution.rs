// LeetCode 0894 - All Possible Full Binary Trees
// https://leetcode.com/problems/all-possible-full-binary-trees/

use std::cell::RefCell;
use std::collections::HashMap;
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
    pub fn all_possible_fbt(n: i32) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        fn clone_tree(node: &Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
            node.as_ref().map(|n| {
                let n = n.borrow();
                Rc::new(RefCell::new(TreeNode {
                    val: n.val,
                    left: clone_tree(&n.left),
                    right: clone_tree(&n.right),
                }))
            })
        }
        fn build(
            nodes: i32,
            memo: &mut HashMap<i32, Vec<Option<Rc<RefCell<TreeNode>>>>>,
        ) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
            if let Some(v) = memo.get(&nodes) {
                return v.clone();
            }
            if nodes % 2 == 0 {
                memo.insert(nodes, vec![]);
                return vec![];
            }
            if nodes == 1 {
                let res = vec![Some(Rc::new(RefCell::new(TreeNode::new(0))))];
                memo.insert(nodes, res.clone());
                return res;
            }
            let mut res = Vec::new();
            let mut left = 1;
            while left < nodes {
                let right = nodes - 1 - left;
                let lefts = build(left, memo);
                let rights = build(right, memo);
                for L in &lefts {
                    for R in &rights {
                        let root = Rc::new(RefCell::new(TreeNode::new(0)));
                        root.borrow_mut().left = clone_tree(L);
                        root.borrow_mut().right = clone_tree(R);
                        res.push(Some(root));
                    }
                }
                left += 2;
            }
            memo.insert(nodes, res.clone());
            res
        }
        let mut memo = HashMap::new();
        build(n, &mut memo)
    }
}
