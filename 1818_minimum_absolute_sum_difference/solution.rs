// LeetCode 1818 - Minimum Absolute Sum Difference
// https://leetcode.com/problems/minimum-absolute-sum-difference/

impl Solution {
    pub fn min_absolute_sum_diff(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut sorted_nums1 = nums1.clone();
        sorted_nums1.sort_unstable();

        let mut total: i64 = 0;
        let mut best_gain = 0i64;

        for i in 0..nums1.len() {
            let current = (nums1[i] - nums2[i]).abs() as i64;
            total += current;
            let target = nums2[i];
            let idx = sorted_nums1.partition_point(|&x| x < target);
            for j in [idx.wrapping_sub(1), idx] {
                if j < sorted_nums1.len() {
                    let gain = current - (sorted_nums1[j] - target).abs() as i64;
                    best_gain = best_gain.max(gain);
                }
            }
        }

        ((total - best_gain) % MOD) as i32
    }
}
