// LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

impl Solution {
    pub fn min_operations(mut nums: Vec<i32>, queries: Vec<i32>) -> Vec<i64> {
        nums.sort_unstable();
        let n = nums.len();
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }
        queries
            .into_iter()
            .map(|q| {
                let i = nums.partition_point(|&x| x < q);
                let left = q as i64 * i as i64 - pref[i];
                let right = pref[n] - pref[i] - q as i64 * (n - i) as i64;
                left + right
            })
            .collect()
    }
}
