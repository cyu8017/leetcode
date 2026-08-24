// LeetCode 2358 - Maximum Number of Groups Entering a Competition
// https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

impl Solution {
    pub fn maximum_groups(grades: Vec<i32>) -> i32 {
        let n = grades.len() as i64;
        let mut k = 0i64;
        while (k + 1) * (k + 2) / 2 <= n {
            k += 1;
        }
        k as i32
    }
}
