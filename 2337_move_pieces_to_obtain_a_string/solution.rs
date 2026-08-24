// LeetCode 2337 - Move Pieces to Obtain a String
// https://leetcode.com/problems/move-pieces-to-obtain-a-string/

impl Solution {
    pub fn can_change(start: String, target: String) -> bool {
        let start = start.as_bytes();
        let target = target.as_bytes();
        let n = start.len();
        let mut i = 0usize;
        let mut j = 0usize;
        while i < n || j < n {
            while i < n && start[i] == b'_' {
                i += 1;
            }
            while j < n && target[j] == b'_' {
                j += 1;
            }
            if i == n || j == n {
                return i == n && j == n;
            }
            if start[i] != target[j] {
                return false;
            }
            if start[i] == b'L' && i < j {
                return false;
            }
            if start[i] == b'R' && i > j {
                return false;
            }
            i += 1;
            j += 1;
        }
        true
    }
}
