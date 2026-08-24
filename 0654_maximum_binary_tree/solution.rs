// LeetCode 0654 - Maximum Binary Tree
// https://leetcode.com/problems/maximum-binary-tree/

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
    fn build(nums: &[i32], left: i32, right: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if left > right {
            return None;
        }
        let mut mid = left;
        for i in left..=right {
            if nums[i as usize] > nums[mid as usize] {
                mid = i;
            }
        }
        Some(Rc::new(RefCell::new(TreeNode {
            val: nums[mid as usize],
            left: Self::build(nums, left, mid - 1),
            right: Self::build(nums, mid + 1, right),
        })))
    }

    pub fn construct_maximum_binary_tree(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        Self::build(&nums, 0, nums.len() as i32 - 1)
    }
}
