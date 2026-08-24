// LeetCode 0968 - Binary Tree Cameras
// https://leetcode.com/problems/binary-tree-cameras/

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
    pub fn min_camera_cover(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, cameras: &mut i32) -> i32 {
            let Some(node) = node else {
                return 1;
            };
            let node = node.borrow();
            let left = dfs(node.left.clone(), cameras);
            let right = dfs(node.right.clone(), cameras);
            if left == 0 || right == 0 {
                *cameras += 1;
                return 2;
            }
            if left == 2 || right == 2 {
                return 1;
            }
            0
        }
        let mut cameras = 0;
        let root_state = dfs(root, &mut cameras);
        cameras + if root_state == 0 { 1 } else { 0 }
    }
}
