// LeetCode 1031 - Maximum Sum of Two Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

impl Solution {
    pub fn max_sum_two_no_overlap(nums: Vec<i32>, first_len: i32, second_len: i32) -> i32 {
        let mut prefix = vec![0; nums.len() + 1];
        for i in 0..nums.len() {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        fn best(prefix: &[i32], a: usize, b: usize) -> i32 {
            let mut best_a = 0;
            let mut ans = 0;
            for i in (a + b)..prefix.len() {
                best_a = best_a.max(prefix[i - b] - prefix[i - b - a]);
                ans = ans.max(best_a + prefix[i] - prefix[i - b]);
            }
            ans
        }
        best(&prefix, first_len as usize, second_len as usize)
            .max(best(&prefix, second_len as usize, first_len as usize))
    }
}
