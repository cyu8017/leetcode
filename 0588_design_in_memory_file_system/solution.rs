// LeetCode 0588 - Design In-Memory File System
// https://leetcode.com/problems/design-in-memory-file-system/

use std::collections::BTreeMap;

struct FsNode {
    is_file: bool,
    content: String,
    children: BTreeMap<String, FsNode>,
}

impl FsNode {
    fn new() -> Self {
        Self {
            is_file: false,
            content: String::new(),
            children: BTreeMap::new(),
        }
    }
}

pub struct FileSystem {
    root: FsNode,
}

impl FileSystem {
    pub fn new() -> Self {
        Self { root: FsNode::new() }
    }

    fn split(path: &str) -> Vec<String> {
        path.split('/')
            .filter(|part| !part.is_empty())
            .map(|part| part.to_string())
            .collect()
    }

    pub fn ls(&self, path: String) -> Vec<String> {
        if path == "/" {
            return self.root.children.keys().cloned().collect();
        }
        let parts = Self::split(&path);
        let mut node = &self.root;
        for part in &parts {
            node = node.children.get(part).unwrap();
        }
        if node.is_file {
            return vec![parts.last().unwrap().clone()];
        }
        node.children.keys().cloned().collect()
    }

    pub fn mkdir(&mut self, path: String) {
        let mut node = &mut self.root;
        for part in Self::split(&path) {
            node = node.children.entry(part).or_insert_with(FsNode::new);
        }
    }

    pub fn add_content_to_file(&mut self, file_path: String, content: String) {
        let parts = Self::split(&file_path);
        let mut node = &mut self.root;
        for part in &parts[..parts.len() - 1] {
            node = node.children.entry(part.clone()).or_insert_with(FsNode::new);
        }
        let name = parts.last().unwrap();
        let file = node.children.entry(name.clone()).or_insert_with(FsNode::new);
        file.is_file = true;
        file.content.push_str(&content);
    }

    pub fn read_content_from_file(&self, file_path: String) -> String {
        let mut node = &self.root;
        for part in Self::split(&file_path) {
            node = node.children.get(&part).unwrap();
        }
        node.content.clone()
    }
}
