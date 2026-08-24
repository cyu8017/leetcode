// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

pub struct LUPrefix {
    uploaded: Vec<bool>,
    prefix_len: i32,
}

impl LUPrefix {
    pub fn new(n: i32) -> Self {
        Self {
            uploaded: vec![false; (n + 2) as usize],
            prefix_len: 0,
        }
    }

    pub fn upload(&mut self, video: i32) {
        self.uploaded[video as usize] = true;
        while self.uploaded[(self.prefix_len + 1) as usize] {
            self.prefix_len += 1;
        }
    }

    pub fn longest(&self) -> i32 {
        self.prefix_len
    }
}

fn main() {}
