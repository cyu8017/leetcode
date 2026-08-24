// LeetCode 3691 - Maximum Total Subarray Value II
// https://leetcode.com/problems/maximum-total-subarray-value-ii/

use std::collections::BinaryHeap;

impl Solution {
    pub fn max_total_value(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut max_log = 0;
        while (1 << max_log) <= n {
            max_log += 1;
        }
        max_log += 1;
        let mut f_max = vec![vec![0; max_log]; n];
        let mut f_min = vec![vec![0; max_log]; n];
        let mut lg = vec![0; n + 1];
        for i in 2..=n {
            lg[i] = lg[i >> 1] + 1;
        }
        for i in 0..n {
            f_max[i][0] = nums[i];
            f_min[i][0] = nums[i];
        }
        for j in 1..max_log {
            let mut i = 0;
            while i + (1 << j) <= n {
                f_max[i][j] = f_max[i][j - 1].max(f_max[i + (1 << (j - 1))][j - 1]);
                f_min[i][j] = f_min[i][j - 1].min(f_min[i + (1 << (j - 1))][j - 1]);
                i += 1;
            }
        }
        let query_max = |l: usize, r: usize| -> i32 {
            let k = lg[r - l + 1];
            f_max[l][k].max(f_max[r - (1 << k) + 1][k])
        };
        let query_min = |l: usize, r: usize| -> i32 {
            let k = lg[r - l + 1];
            f_min[l][k].min(f_min[r - (1 << k) + 1][k])
        };
        let mut pq: BinaryHeap<(i64, usize, usize)> = BinaryHeap::new();
        for l in 0..n {
            let val = query_max(l, n - 1) as i64 - query_min(l, n - 1) as i64;
            pq.push((val, l, n - 1));
        }
        let mut ans = 0i64;
        for _ in 0..k {
            let (val, l, r) = pq.pop().unwrap();
            ans += val;
            if r > l {
                let next_val = query_max(l, r - 1) as i64 - query_min(l, r - 1) as i64;
                pq.push((next_val, l, r - 1));
            }
        }
        ans
    }
}
