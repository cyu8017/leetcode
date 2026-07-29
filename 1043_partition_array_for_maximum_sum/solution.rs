// LeetCode 1043 - Partition Array for Maximum Sum
// https://leetcode.com/problems/partition-array-for-maximum-sum/

impl Solution {
    pub fn max_sum_after_partitioning(arr: Vec<i32>, k: i32) -> i32 {
        let n = arr.len();
        let k = k as usize;
        let mut dp = vec![0; n + 1];
        for i in 1..=n {
            let mut best = 0;
            for size in 1..=k.min(i) {
                best = best.max(arr[i - size]);
                dp[i] = dp[i].max(dp[i - size] + best * size as i32);
            }
        }
        dp[n]
    }
}
