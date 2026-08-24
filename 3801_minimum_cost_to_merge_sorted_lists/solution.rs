// LeetCode 3801 - Minimum Cost to Merge Sorted Lists
// https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

impl Solution {
    pub fn min_merge_cost(lists: Vec<Vec<i32>>) -> i64 {
        let m = lists.len();
        let total_masks = 1 << m;
        let mut merged = vec![Vec::new(); total_masks];
        let mut length = vec![0i32; total_masks];
        let mut median = vec![0i32; total_masks];
        for mask in 1..total_masks {
            let bit = mask & mask.wrapping_neg();
            let mut index = 0;
            while (1 << index) != bit {
                index += 1;
            }
            let previous = &merged[mask ^ bit];
            let current = &lists[index];
            let mut out = Vec::with_capacity(previous.len() + current.len());
            let mut i = 0;
            let mut j = 0;
            while i < previous.len() || j < current.len() {
                if j == current.len() || (i < previous.len() && previous[i] <= current[j]) {
                    out.push(previous[i]);
                    i += 1;
                } else {
                    out.push(current[j]);
                    j += 1;
                }
            }
            length[mask] = out.len() as i32;
            median[mask] = out[(out.len() - 1) / 2];
            merged[mask] = out;
        }
        const INF: i64 = 1i64 << 62;
        let mut dp = vec![0i64; total_masks];
        for mask in 1..total_masks {
            if (mask & (mask - 1)) == 0 {
                continue;
            }
            dp[mask] = INF;
            let first_bit = mask & mask.wrapping_neg();
            let mut left = (mask - 1) & mask;
            while left > 0 {
                if (left & first_bit) != 0 {
                    let right = mask ^ left;
                    if right != 0 {
                        let mut diff = median[left] - median[right];
                        if diff < 0 {
                            diff = -diff;
                        }
                        let candidate = dp[left] + dp[right] + length[mask] as i64 + diff as i64;
                        if candidate < dp[mask] {
                            dp[mask] = candidate;
                        }
                    }
                }
                left = (left - 1) & mask;
            }
        }
        dp[total_masks - 1]
    }
}
