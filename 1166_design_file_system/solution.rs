// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

use std::collections::HashMap;

struct FileSystem {
    vals: HashMap<String, i32>,
}

impl FileSystem {
    fn new() -> Self {
        Self {
            vals: HashMap::new(),
        }
    }

    fn create_path(&mut self, path: String, value: i32) -> bool {
        if path == "/" || self.vals.contains_key(&path) {
            return false;
        }
        if let Some(idx) = path.rfind('/') {
            let parent = &path[..idx];
            if !parent.is_empty() && !self.vals.contains_key(parent) {
                return false;
            }
        }
        self.vals.insert(path, value);
        true
    }

    fn get(&self, path: String) -> i32 {
        *self.vals.get(&path).unwrap_or(&-1)
    }
}
