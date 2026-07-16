// LeetCode 0297 - Serialize and Deserialize Binary Tree
// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

struct Codec;

impl Codec {
    pub fn serialize(&self, root: Option<Rc<RefCell<TreeNode>>>) -> String {
        if root.is_none() {
            return String::new();
        }

        let mut values = Vec::new();
        let mut queue = VecDeque::new();
        queue.push_back(root);

        while let Some(node) = queue.pop_front() {
            if let Some(node) = node {
                values.push(node.borrow().val.to_string());
                queue.push_back(node.borrow().left.clone());
                queue.push_back(node.borrow().right.clone());
            } else {
                values.push(String::new());
            }
        }

        while values.last().map(String::is_empty).unwrap_or(false) {
            values.pop();
        }

        values.join(",")
    }

    pub fn deserialize(&self, data: String) -> Option<Rc<RefCell<TreeNode>>> {
        if data.is_empty() {
            return None;
        }

        let values: Vec<&str> = data.split(',').collect();
        let root = Rc::new(RefCell::new(TreeNode {
            val: values[0].parse().unwrap(),
            left: None,
            right: None,
        }));

        let mut queue = VecDeque::new();
        queue.push_back(root.clone());
        let mut index = 1;

        while let Some(node) = queue.pop_front() {
            if index < values.len() && !values[index].is_empty() {
                let left = Rc::new(RefCell::new(TreeNode {
                    val: values[index].parse().unwrap(),
                    left: None,
                    right: None,
                }));
                node.borrow_mut().left = Some(left.clone());
                queue.push_back(left);
            }
            index += 1;

            if index < values.len() && !values[index].is_empty() {
                let right = Rc::new(RefCell::new(TreeNode {
                    val: values[index].parse().unwrap(),
                    left: None,
                    right: None,
                }));
                node.borrow_mut().right = Some(right.clone());
                queue.push_back(right);
            }
            index += 1;
        }

        Some(root)
    }
}
