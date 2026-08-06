// LeetCode 1110 - Delete Nodes And Return Forest
// https://leetcode.com/problems/delete-nodes-and-return-forest/

use std::cell::RefCell;
use std::collections::HashSet;
use std::rc::Rc;

impl Solution {
    pub fn del_nodes(
        root: Option<Rc<RefCell<TreeNode>>>,
        to_delete: Vec<i32>,
    ) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        let delete_set: HashSet<i32> = to_delete.into_iter().collect();
        let mut forest = Vec::new();
        Self::dfs(root, true, &delete_set, &mut forest);
        forest
    }

    fn dfs(
        node: Option<Rc<RefCell<TreeNode>>>,
        is_root: bool,
        delete_set: &HashSet<i32>,
        forest: &mut Vec<Option<Rc<RefCell<TreeNode>>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let node = match node {
            Some(n) => n,
            None => return None,
        };
        let val = node.borrow().val;
        let removed = delete_set.contains(&val);
        if is_root && !removed {
            forest.push(Some(node.clone()));
        }
        let left = node.borrow().left.clone();
        let right = node.borrow().right.clone();
        let new_left = Self::dfs(left, removed, delete_set, forest);
        let new_right = Self::dfs(right, removed, delete_set, forest);
        node.borrow_mut().left = new_left;
        node.borrow_mut().right = new_right;
        if removed {
            None
        } else {
            Some(node)
        }
    }
}
