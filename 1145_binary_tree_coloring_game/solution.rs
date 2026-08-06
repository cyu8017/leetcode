// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    pub fn btree_game_winning_move(
        root: Option<Rc<RefCell<TreeNode>>>,
        n: i32,
        x: i32,
    ) -> bool {
        let mut left = 0;
        let mut right = 0;
        Self::dfs(root, x, &mut left, &mut right);
        let parent_side = n - left - right - 1;
        let best = left.max(right).max(parent_side);
        best > n / 2
    }

    fn dfs(
        node: Option<Rc<RefCell<TreeNode>>>,
        x: i32,
        left: &mut i32,
        right: &mut i32,
    ) -> i32 {
        let node = match node {
            Some(n) => n,
            None => return 0,
        };
        let b = node.borrow();
        let l = Self::dfs(b.left.clone(), x, left, right);
        let r = Self::dfs(b.right.clone(), x, left, right);
        if b.val == x {
            *left = l;
            *right = r;
        }
        l + r + 1
    }
}
