// LeetCode 3648 - Minimum Sensors to Cover Grid
// https://leetcode.com/problems/minimum-sensors-to-cover-grid/

impl Solution {
    pub fn min_sensors(n: i32, m: i32, k: i32) -> i32 {
        let cover = 2 * k + 1;
        ((n + cover - 1) / cover) * ((m + cover - 1) / cover)
    }
}
