// LeetCode 1540 - Can Convert String in K Moves
// https://leetcode.com/problems/can-convert-string-in-k-moves/

impl Solution {
    pub fn can_convert_string(s: String, t: String, k: i32) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut used = [0i32; 26];
        for (a, b) in s.bytes().zip(t.bytes()) {
            let shift = ((b as i32 - a as i32) + 26) % 26;
            if shift == 0 {
                continue;
            }
            used[shift as usize] += 1;
            if shift + 26 * (used[shift as usize] - 1) > k {
                return false;
            }
        }
        true
    }
}
