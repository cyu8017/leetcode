// LeetCode 1787 - Make the XOR of All Segments Equal to Zero
// https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

impl Solution {
    pub fn min_changes(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut freq = vec![vec![0i32; 1024]; k];
        let mut size = vec![0i32; k];
        for (i, &x) in nums.iter().enumerate() {
            freq[i % k][x as usize] += 1;
            size[i % k] += 1;
        }
        const INF: i32 = 1_000_000_000;
        let mut dp = vec![INF; 256];
        dp[0] = 0;
        for i in 0..k {
            let mut ndp = vec![INF; 256];
            for xv in 0..256usize {
                let cost = size[i] - freq[i][xv];
                for xo in 0..256usize {
                    if dp[xo] == INF {
                        continue;
                    }
                    let key = xo ^ xv;
                    if dp[xo] + cost < ndp[key] {
                        ndp[key] = dp[xo] + cost;
                    }
                }
            }
            dp = ndp;
        }
        dp[0]
    }
}
