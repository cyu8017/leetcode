// LeetCode 3237 - Alt and Tab Simulation
// https://leetcode.com/problems/alt-and-tab-simulation/

impl Solution {
    pub fn simulation_result(windows: Vec<i32>, queries: Vec<i32>) -> Vec<i32> {
        let n = windows.len();
        let mut s = vec![false; n + 1];
        let mut ans = Vec::new();
        for &q in queries.iter().rev() {
            if !s[q as usize] {
                s[q as usize] = true;
                ans.push(q);
            }
        }
        for w in windows {
            if !s[w as usize] {
                ans.push(w);
            }
        }
        ans
    }
}
