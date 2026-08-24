// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/

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
    pub fn count_great_enough_nodes(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
        let mut ans = 0;
        Self::dfs(root, k, &mut ans);
        ans
    }

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, k: i32, ans: &mut i32) -> Vec<i32> {
        let Some(n) = node else {
            return vec![];
        };
        let val = n.borrow().val;
        let left = n.borrow().left.clone();
        let right = n.borrow().right.clone();
        let mut vals = vec![val];
        vals.extend(Self::dfs(left, k, ans));
        vals.extend(Self::dfs(right, k, ans));
        let smaller = vals.iter().filter(|&&v| v < val).count() as i32;
        if smaller >= k {
            *ans += 1;
        }
        vals
    }
}
