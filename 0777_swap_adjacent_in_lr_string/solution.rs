// LeetCode 0777 - Swap Adjacent in LR String
// https://leetcode.com/problems/swap-adjacent-in-lr-string/

impl Solution {
    pub fn can_transform(start: String, result: String) -> bool {
        let a: String = start.chars().filter(|&ch| ch != 'X').collect();
        let b: String = result.chars().filter(|&ch| ch != 'X').collect();
        if a != b {
            return false;
        }
        let start: Vec<char> = start.chars().collect();
        let result: Vec<char> = result.chars().collect();
        let n = start.len();
        let mut i = 0;
        let mut j = 0;
        while i < n && j < n {
            while i < n && start[i] == 'X' {
                i += 1;
            }
            while j < n && result[j] == 'X' {
                j += 1;
            }
            if i == n || j == n {
                break;
            }
            if start[i] != result[j] {
                return false;
            }
            if start[i] == 'L' && i < j {
                return false;
            }
            if start[i] == 'R' && i > j {
                return false;
            }
            i += 1;
            j += 1;
        }
        true
    }
}
