// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

impl Solution {
    pub fn min_increment_operations(nums: Vec<i32>, k: i32) -> i64 {
        let mut dp0 = 0i64;
        let mut dp1 = 0i64;
        let mut dp2 = 0i64;
        for v in nums {
            let cost = if v < k { (k - v) as i64 } else { 0 };
            let nd0 = cost + dp0.min(dp1).min(dp2);
            dp0 = dp1;
            dp1 = dp2;
            dp2 = nd0;
        }
        dp0.min(dp1).min(dp2)
    }
}
