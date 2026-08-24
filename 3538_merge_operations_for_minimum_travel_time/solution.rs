// LeetCode 3538 - Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

use std::collections::HashMap;

impl Solution {
    pub fn min_travel_time(_l: i32, n: i32, k: i32, position: Vec<i32>, time: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut prefix = vec![0i32; n];
        prefix[0] = time[0];
        for i in 1..n {
            prefix[i] = prefix[i - 1] + time[i];
        }
        const INF: i64 = 1_000_000_000_000_000_000;
        fn dp(
            i: usize,
            skips: i32,
            last: usize,
            n: usize,
            prefix: &[i32],
            position: &[i32],
            memo: &mut HashMap<(usize, i32, usize), i64>,
        ) -> i64 {
            if i == n - 1 {
                return if skips == 0 { 0 } else { INF };
            }
            let key = (i, skips, last);
            if let Some(&v) = memo.get(&key) {
                return v;
            }
            let mut rate = prefix[i];
            if last > 0 {
                rate -= prefix[last - 1];
            }
            let mut res = INF;
            let mut end = n - 1;
            if i + skips as usize + 1 < end {
                end = i + skips as usize + 1;
            }
            for j in i + 1..=end {
                let cand = (position[j] - position[i]) as i64 * rate as i64
                    + dp(j, skips - (j - i - 1) as i32, i + 1, n, prefix, position, memo);
                if cand < res {
                    res = cand;
                }
            }
            memo.insert(key, res);
            res
        }
        let mut memo = HashMap::new();
        dp(0, k, 0, n, &prefix, &position, &mut memo) as i32
    }
}
