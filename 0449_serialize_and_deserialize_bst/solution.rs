// LeetCode 0449 - Serialize and Deserialize BST
// https://leetcode.com/problems/serialize-and-deserialize-bst/

use std::cell::RefCell;
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
        let mut parts = Vec::new();

        fn preorder(node: Option<Rc<RefCell<TreeNode>>>, parts: &mut Vec<String>) {
            match node {
                None => parts.push("#".to_string()),
                Some(node) => {
                    parts.push(node.borrow().val.to_string());
                    preorder(node.borrow().left.clone(), parts);
                    preorder(node.borrow().right.clone(), parts);
                }
            }
        }

        preorder(root, &mut parts);
        parts.join(",")
    }

    pub fn deserialize(&self, data: String) -> Option<Rc<RefCell<TreeNode>>> {
        if data.is_empty() {
            return None;
        }

        let values: Vec<&str> = data.split(',').collect();
        let mut index = 0;

        fn build(values: &[&str], index: &mut usize) -> Option<Rc<RefCell<TreeNode>>> {
            let token = values[*index];
            *index += 1;
            if token == "#" {
                return None;
            }
            let node = Rc::new(RefCell::new(TreeNode {
                val: token.parse().unwrap(),
                left: None,
                right: None,
            }));
            node.borrow_mut().left = build(values, index);
            node.borrow_mut().right = build(values, index);
            Some(node)
        }

        build(&values, &mut index)
    }
}
