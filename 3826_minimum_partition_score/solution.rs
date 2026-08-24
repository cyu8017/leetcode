// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum-partition-score/

impl Solution {
    pub fn min_partition_score(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut prefix = vec![0i64; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + nums[i] as i64;
        }
        let value = |left: usize, right: usize| {
            let sum = prefix[right] - prefix[left];
            sum * (sum + 1) / 2
        };
        const INF: i64 = 1i64 << 62;
        let mut previous = vec![INF; n + 1];
        previous[0] = 0;
        for parts in 1..=k {
            let mut current = vec![INF; n + 1];
            fn compute(
                lo: usize,
                hi: i32,
                opt_lo: usize,
                opt_hi: usize,
                previous: &[i64],
                current: &mut [i64],
                value: &dyn Fn(usize, usize) -> i64,
            ) {
                if lo as i32 > hi {
                    return;
                }
                let mid = (lo as i32 + hi) as usize / 2;
                let mut best_index = None;
                let end = opt_hi.min(mid.saturating_sub(1));
                for split in opt_lo..=end {
                    if previous[split] == INF {
                        continue;
                    }
                    let candidate = previous[split] + value(split, mid);
                    if candidate < current[mid] {
                        current[mid] = candidate;
                        best_index = Some(split);
                    }
                }
                let best_index = best_index.unwrap_or(opt_lo);
                if mid > 0 {
                    compute(lo, mid as i32 - 1, opt_lo, best_index, previous, current, value);
                }
                compute(mid + 1, hi, best_index, opt_hi, previous, current, value);
            }
            compute(parts as usize, n as i32, (parts - 1) as usize, n.saturating_sub(1), &previous, &mut current, &value);
            previous = current;
        }
        previous[n]
    }
}
