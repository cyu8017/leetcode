// LeetCode 1948 - Delete Duplicate Folders in System
// https://leetcode.com/problems/delete-duplicate-folders-in-system/

use std::collections::{BTreeMap, HashMap};

struct Node {
    children: BTreeMap<String, Node>,
    serial: String,
    del: bool,
}

impl Node {
    fn new() -> Self {
        Self {
            children: BTreeMap::new(),
            serial: String::new(),
            del: false,
        }
    }
}

impl Solution {
    pub fn delete_duplicate_folder(paths: Vec<Vec<String>>) -> Vec<Vec<String>> {
        let mut root = Node::new();
        for path in paths {
            let mut cur = &mut root;
            for folder in path {
                cur = cur
                    .children
                    .entry(folder)
                    .or_insert_with(Node::new);
            }
        }

        let mut freq: HashMap<String, i32> = HashMap::new();
        Self::serialize(&mut root, &mut freq);
        Self::mark(&mut root, &freq);

        let mut ans = Vec::new();
        Self::collect(&root, &mut Vec::new(), &mut ans);
        ans
    }

    fn serialize(node: &mut Node, freq: &mut HashMap<String, i32>) -> String {
        if node.children.is_empty() {
            return String::new();
        }
        let mut sb = String::new();
        // Collect keys first to avoid borrow issues while mutating children
        let keys: Vec<String> = node.children.keys().cloned().collect();
        for key in keys {
            let child_serial = {
                let child = node.children.get_mut(&key).unwrap();
                Self::serialize(child, freq)
            };
            sb.push_str(&key);
            sb.push('(');
            sb.push_str(&child_serial);
            sb.push(')');
        }
        node.serial = sb.clone();
        *freq.entry(sb.clone()).or_insert(0) += 1;
        sb
    }

    fn mark(node: &mut Node, freq: &HashMap<String, i32>) {
        if !node.serial.is_empty() && freq.get(&node.serial).copied().unwrap_or(0) > 1 {
            node.del = true;
            return;
        }
        for child in node.children.values_mut() {
            Self::mark(child, freq);
        }
    }

    fn collect(node: &Node, path: &mut Vec<String>, ans: &mut Vec<Vec<String>>) {
        for (name, child) in &node.children {
            if child.del {
                continue;
            }
            path.push(name.clone());
            ans.push(path.clone());
            Self::collect(child, path, ans);
            path.pop();
        }
    }
}
