// LeetCode 2611 - Mice and Cheese
// https://leetcode.com/problems/mice-and-cheese/

impl Solution {
    pub fn mice_and_cheese(reward1: Vec<i32>, reward2: Vec<i32>, k: i32) -> i32 {
        let n = reward1.len();
        let mut diff = vec![0; n];
        let mut ans = 0;
        for i in 0..n {
            ans += reward2[i];
            diff[i] = reward1[i] - reward2[i];
        }
        diff.sort_by(|a, b| b.cmp(a));
        for i in 0..k as usize {
            ans += diff[i];
        }
        ans
    }
}
