// LeetCode 0108 - Convert Sorted Array to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

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
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        Self::build(&nums, 0, nums.len() as i32 - 1)
    }

    fn build(nums: &[i32], left: i32, right: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if left > right {
            return None;
        }
        let mid = (left + right + 1) / 2;
        let mut root = TreeNode::new(nums[mid as usize]);
        root.left = Self::build(nums, left, mid - 1);
        root.right = Self::build(nums, mid + 1, right);
        Some(Rc::new(RefCell::new(root)))
    }
}
