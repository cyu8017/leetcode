// LeetCode 1932 - Merge BSTs to Create Single BST
// https://leetcode.com/problems/merge-bsts-to-create-single-bst/

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
    pub fn can_merge(trees: Vec<Option<Rc<RefCell<TreeNode>>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let trees: Vec<Rc<RefCell<TreeNode>>> = trees.into_iter().flatten().collect();
        let mut value_to_root: HashMap<i32, Rc<RefCell<TreeNode>>> = HashMap::new();
        let mut count: HashMap<i32, i32> = HashMap::new();

        for tree in &trees {
            let val = tree.borrow().val;
            value_to_root.insert(val, Rc::clone(tree));
            *count.entry(val).or_insert(0) += 1;
            let left_val = tree.borrow().left.as_ref().map(|n| n.borrow().val);
            let right_val = tree.borrow().right.as_ref().map(|n| n.borrow().val);
            if let Some(v) = left_val {
                *count.entry(v).or_insert(0) += 1;
            }
            if let Some(v) = right_val {
                *count.entry(v).or_insert(0) += 1;
            }
        }

        let roots: Vec<_> = trees
            .iter()
            .filter(|t| count[&t.borrow().val] == 1)
            .cloned()
            .collect();
        if roots.len() != 1 {
            return None;
        }
        let root = roots[0].clone();
        value_to_root.remove(&root.borrow().val);

        if !Self::merge(&root, &mut value_to_root) || !value_to_root.is_empty() {
            return None;
        }

        if Self::is_valid_bst(&root, i64::MIN, i64::MAX) {
            Some(root)
        } else {
            None
        }
    }

    fn merge(
        node: &Rc<RefCell<TreeNode>>,
        value_to_root: &mut HashMap<i32, Rc<RefCell<TreeNode>>>,
    ) -> bool {
        let (left_opt, right_opt) = {
            let n = node.borrow();
            (n.left.clone(), n.right.clone())
        };

        if let Some(ref left) = left_opt {
            let lv = left.borrow().val;
            if value_to_root.contains_key(&lv) {
                let replacement = value_to_root.remove(&lv).unwrap();
                node.borrow_mut().left = Some(replacement);
            }
        }
        if let Some(ref right) = right_opt {
            let rv = right.borrow().val;
            if value_to_root.contains_key(&rv) {
                let replacement = value_to_root.remove(&rv).unwrap();
                node.borrow_mut().right = Some(replacement);
            }
        }

        let (left, right) = {
            let n = node.borrow();
            (n.left.clone(), n.right.clone())
        };

        let left_ok = match left {
            Some(l) => Self::merge(&l, value_to_root),
            None => true,
        };
        let right_ok = match right {
            Some(r) => Self::merge(&r, value_to_root),
            None => true,
        };
        left_ok && right_ok
    }

    fn is_valid_bst(node: &Rc<RefCell<TreeNode>>, lo: i64, hi: i64) -> bool {
        let n = node.borrow();
        let val = n.val as i64;
        if !(lo < val && val < hi) {
            return false;
        }
        let left_ok = match &n.left {
            Some(l) => Self::is_valid_bst(l, lo, val),
            None => true,
        };
        let right_ok = match &n.right {
            Some(r) => Self::is_valid_bst(r, val, hi),
            None => true,
        };
        left_ok && right_ok
    }
}
