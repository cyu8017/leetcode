// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

use std::cell::RefCell;
use std::collections::HashSet;
use std::rc::Rc;

struct FindElements {
    values: HashSet<i32>,
}

impl FindElements {
    fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {
        let mut values = HashSet::new();
        fn recover(node: Option<Rc<RefCell<TreeNode>>>, value: i32, values: &mut HashSet<i32>) {
            let Some(node) = node else { return };
            node.borrow_mut().val = value;
            values.insert(value);
            let (left, right) = {
                let b = node.borrow();
                (b.left.clone(), b.right.clone())
            };
            recover(left, 2 * value + 1, values);
            recover(right, 2 * value + 2, values);
        }
        recover(root, 0, &mut values);
        Self { values }
    }

    fn find(&self, target: i32) -> bool {
        self.values.contains(&target)
    }
}
