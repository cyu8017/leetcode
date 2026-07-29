// LeetCode 1014 - Best Sightseeing Pair
// https://leetcode.com/problems/best-sightseeing-pair/

impl Solution {
    pub fn max_score_sightseeing_pair(values: Vec<i32>) -> i32 {
        let mut best = values[0];
        let mut ans = 0;
        for j in 1..values.len() {
            ans = ans.max(best + values[j] - j as i32);
            best = best.max(values[j] + j as i32);
        }
        ans
    }
}
