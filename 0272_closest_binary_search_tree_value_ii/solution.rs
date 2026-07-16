// LeetCode 0272 - Closest Binary Search Tree Value II
// https://leetcode.com/problems/closest-binary-search-tree-value-ii/

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
    pub fn closest_k_values(root: Option<Rc<RefCell<TreeNode>>>, target: f64, k: i32) -> Vec<i32> {
        let mut values = Vec::new();
        Self::inorder(&root, &mut values);

        let mut lo = 0usize;
        let mut hi = values.len();
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if (values[mid] as f64) < target {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        let mut left = lo as i32 - 1;
        let mut right = lo as i32;
        let mut result = Vec::new();
        while result.len() < k as usize {
            if right as usize >= values.len()
                || (left >= 0
                    && (values[left as usize] as f64 - target).abs()
                        <= (values[right as usize] as f64 - target).abs())
            {
                result.push(values[left as usize]);
                left -= 1;
            } else {
                result.push(values[right as usize]);
                right += 1;
            }
        }
        result
    }

    fn inorder(node: &Option<Rc<RefCell<TreeNode>>>, values: &mut Vec<i32>) {
        if let Some(current) = node {
            let (left, right, val) = {
                let borrowed = current.borrow();
                (
                    borrowed.left.clone(),
                    borrowed.right.clone(),
                    borrowed.val,
                )
            };
            Self::inorder(&left, values);
            values.push(val);
            Self::inorder(&right, values);
        }
    }
}
