// LeetCode 2399 - Check Distances Between Same Letters
// https://leetcode.com/problems/check-distances-between-same-letters/

impl Solution {
    pub fn check_distances(s: String, distance: Vec<i32>) -> bool {
        let mut first = [-1i32; 26];
        for (i, c) in s.bytes().enumerate() {
            let c = (c - b'a') as usize;
            if first[c] == -1 {
                first[c] = i as i32;
            } else if i as i32 - first[c] - 1 != distance[c] {
                return false;
            }
        }
        true
    }
}
