// LeetCode 1500 - Design a File Sharing System
// https://leetcode.com/problems/design-a-file-sharing-system/

use std::collections::{BinaryHeap, HashMap, HashSet};
use std::cmp::Reverse;

pub struct FileSharing {
    owners: HashMap<i32, HashSet<i32>>,
    chunks: HashMap<i32, HashSet<i32>>,
    free: BinaryHeap<Reverse<i32>>,
    next_id: i32,
}

impl FileSharing {
    pub fn new(_m: i32) -> Self {
        Self {
            owners: HashMap::new(),
            chunks: HashMap::new(),
            free: BinaryHeap::new(),
            next_id: 1,
        }
    }

    pub fn join(&mut self, owned_chunks: Vec<i32>) -> i32 {
        let user = if let Some(Reverse(id)) = self.free.pop() {
            id
        } else {
            let id = self.next_id;
            self.next_id += 1;
            id
        };
        let set: HashSet<i32> = owned_chunks.into_iter().collect();
        for &chunk in &set {
            self.owners.entry(chunk).or_default().insert(user);
        }
        self.chunks.insert(user, set);
        user
    }

    pub fn leave(&mut self, user_id: i32) {
        if let Some(chunks) = self.chunks.remove(&user_id) {
            for chunk in chunks {
                if let Some(owners) = self.owners.get_mut(&chunk) {
                    owners.remove(&user_id);
                }
            }
        }
        self.free.push(Reverse(user_id));
    }

    pub fn request(&mut self, user_id: i32, chunk_id: i32) -> Vec<i32> {
        let mut users: Vec<i32> = self
            .owners
            .get(&chunk_id)
            .map(|s| s.iter().copied().collect())
            .unwrap_or_default();
        users.sort_unstable();
        if !users.is_empty() {
            self.chunks.entry(user_id).or_default().insert(chunk_id);
            self.owners.entry(chunk_id).or_default().insert(user_id);
        }
        users
    }
}
