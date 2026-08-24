// LeetCode 3522 - Calculate Score After Performing Instructions
// https://leetcode.com/problems/calculate-score-after-performing-instructions/

impl Solution {
    pub fn calculate_score(instructions: Vec<String>, values: Vec<i32>) -> i64 {
        let n = values.len();
        let mut vis = vec![false; n];
        let mut ans = 0i64;
        let mut i: i32 = 0;
        while i >= 0 && (i as usize) < n && !vis[i as usize] {
            vis[i as usize] = true;
            if instructions[i as usize].as_bytes()[0] == b'a' {
                ans += values[i as usize] as i64;
                i += 1;
            } else {
                i += values[i as usize];
            }
        }
        ans
    }
}
