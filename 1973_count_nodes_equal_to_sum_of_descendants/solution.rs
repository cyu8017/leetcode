// LeetCode 1973 - Count Nodes Equal to Sum of Descendants
// https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

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
    pub fn equal_to_descendants(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, ans: &mut i32) -> i64 {
            match node {
                None => 0,
                Some(rc) => {
                    let n = rc.borrow();
                    let total = dfs(n.left.clone(), ans) + dfs(n.right.clone(), ans);
                    if total == n.val as i64 {
                        *ans += 1;
                    }
                    total + n.val as i64
                }
            }
        }
        let mut ans = 0;
        dfs(root, &mut ans);
        ans
    }
}
