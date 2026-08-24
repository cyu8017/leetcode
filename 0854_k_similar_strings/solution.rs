// LeetCode 0854 - K-Similar Strings
// https://leetcode.com/problems/k-similar-strings/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn k_similarity(s1: String, s2: String) -> i32 {
        if s1 == s2 {
            return 0;
        }
        let target: Vec<u8> = s2.into_bytes();
        let mut queue = VecDeque::new();
        queue.push_back((s1.clone().into_bytes(), 0));
        let mut seen = HashSet::from([s1]);
        while let Some((cur, dist)) = queue.pop_front() {
            for nxt in Self::neighbors(&cur, &target) {
                if nxt == target {
                    return dist + 1;
                }
                let key = String::from_utf8(nxt.clone()).unwrap();
                if seen.insert(key) {
                    queue.push_back((nxt, dist + 1));
                }
            }
        }
        -1
    }

    fn neighbors(s: &[u8], target: &[u8]) -> Vec<Vec<u8>> {
        let mut arr = s.to_vec();
        let mut i = 0;
        while arr[i] == target[i] {
            i += 1;
        }
        let mut res = Vec::new();
        for j in i + 1..arr.len() {
            if arr[j] == target[i] && arr[j] != target[j] {
                arr.swap(i, j);
                res.push(arr.clone());
                arr.swap(i, j);
            }
        }
        res
    }
}
