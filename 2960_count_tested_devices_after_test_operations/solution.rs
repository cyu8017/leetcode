// LeetCode 2960 - Count Tested Devices After Test Operations
// https://leetcode.com/problems/count-tested-devices-after-test-operations/

impl Solution {
    pub fn count_tested_devices(battery_percentages: Vec<i32>) -> i32 {
        let mut ans = 0;
        for b in battery_percentages {
            if b > ans {
                ans += 1;
            }
        }
        ans
    }
}
