// LeetCode 0428 - Serialize and Deserialize N-ary Tree
// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub children: Vec<Rc<RefCell<Node>>>,
}

struct Codec;

impl Codec {
    pub fn serialize(&self, root: Option<Rc<RefCell<Node>>>) -> String {
        let Some(root) = root else {
            return String::new();
        };

        let mut parts = Vec::new();
        let mut queue = VecDeque::new();
        queue.push_back(root);

        while let Some(node) = queue.pop_front() {
            let node = node.borrow();
            parts.push(node.val.to_string());
            parts.push(node.children.len().to_string());
            for child in &node.children {
                parts.push(child.borrow().val.to_string());
                queue.push_back(child.clone());
            }
        }

        parts.join(",")
    }

    pub fn deserialize(&self, data: String) -> Option<Rc<RefCell<Node>>> {
        if data.is_empty() {
            return None;
        }

        let values: Vec<&str> = data.split(',').collect();
        let mut index = 0;

        let read_root = |index: &mut usize| -> Rc<RefCell<Node>> {
            let value: i32 = values[*index].parse().unwrap();
            let child_count: usize = values[*index + 1].parse().unwrap();
            *index += 2;
            let node = Rc::new(RefCell::new(Node {
                val: value,
                children: Vec::new(),
            }));
            for _ in 0..child_count {
                let child_value: i32 = values[*index].parse().unwrap();
                node.borrow_mut().children.push(Rc::new(RefCell::new(Node {
                    val: child_value,
                    children: Vec::new(),
                })));
                *index += 1;
            }
            node
        };

        let root = read_root(&mut index);
        let mut queue: VecDeque<Rc<RefCell<Node>>> = root
            .borrow()
            .children
            .iter()
            .cloned()
            .collect();

        while let Some(node) = queue.pop_front() {
            let value: i32 = values[index].parse().unwrap();
            let child_count: usize = values[index + 1].parse().unwrap();
            index += 2;
            if value != node.borrow().val {
                return None;
            }
            for _ in 0..child_count {
                let child_value: i32 = values[index].parse().unwrap();
                let child = Rc::new(RefCell::new(Node {
                    val: child_value,
                    children: Vec::new(),
                }));
                node.borrow_mut().children.push(child.clone());
                queue.push_back(child);
                index += 1;
            }
        }

        Some(root)
    }
}
