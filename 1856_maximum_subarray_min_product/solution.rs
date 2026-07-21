// LeetCode 1856 - Maximum Subarray Min-Product
// https://leetcode.com/problems/maximum-subarray-min-product/

impl Solution {
    pub fn max_sum_min_product(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let mut prefix = vec![0i64; n + 1];
        for (i, &value) in nums.iter().enumerate() {
            prefix[i + 1] = prefix[i] + value as i64;
        }

        let mut left_bound = vec![-1isize; n];
        let mut stack: Vec<usize> = Vec::new();
        for (i, &value) in nums.iter().enumerate() {
            while stack.last().is_some_and(|&j| nums[j] >= value) {
                stack.pop();
            }
            left_bound[i] = stack.last().map(|&j| j as isize).unwrap_or(-1);
            stack.push(i);
        }

        let mut right_bound = vec![n; n];
        stack.clear();
        for i in (0..n).rev() {
            let value = nums[i];
            while stack.last().is_some_and(|&j| nums[j] >= value) {
                stack.pop();
            }
            right_bound[i] = stack.last().copied().unwrap_or(n);
            stack.push(i);
        }

        let mut best = 0i64;
        for (i, &value) in nums.iter().enumerate() {
            let total = prefix[right_bound[i]] - prefix[(left_bound[i] + 1) as usize];
            best = best.max(total * value as i64);
        }
        (best % MOD) as i32
    }
}
