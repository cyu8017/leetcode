// LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
// https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn minimum_flips(root: Option<Rc<RefCell<TreeNode>>>, result: bool) -> i32 {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>) -> (i32, i32) {
            let node = node.as_ref().unwrap().borrow();
            if node.left.is_none() && node.right.is_none() {
                return if node.val == 0 { (0, 1) } else { (1, 0) };
            }
            if node.val == 5 {
                let (f, t) = dfs(&node.left);
                return (t, f);
            }
            let (lf, lt) = dfs(&node.left);
            let (rf, rt) = dfs(&node.right);
            match node.val {
                2 => (lf + rf, (lt + rt).min(lt + rf).min(lf + rt)),
                3 => ((lf + rf).min(lf + rt).min(lt + rf), lt + rt),
                4 => ((lf + rf).min(lt + rt), (lf + rt).min(lt + rf)),
                _ => (0, 0),
            }
        }
        let (f, t) = dfs(&root);
        if result { t } else { f }
    }
}
