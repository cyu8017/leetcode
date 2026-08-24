// LeetCode 3883 - Count Non-Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

impl Solution {
    pub fn count_non_decreasing_arrays(digit_sum: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut groups: Vec<Vec<i32>> = vec![Vec::new(); 51];
        for x in 0..=5000 {
            let mut s = 0;
            let mut y = x;
            while y > 0 {
                s += y % 10;
                y /= 10;
            }
            groups[s as usize].push(x);
        }
        let mut prev_vals = groups[digit_sum[0] as usize].clone();
        let mut dp = vec![1; prev_vals.len()];
        for pos in 1..digit_sum.len() {
            let cur_vals = &groups[digit_sum[pos] as usize];
            let mut next = vec![0; cur_vals.len()];
            let mut j = 0;
            let mut prefix = 0;
            for i in 0..cur_vals.len() {
                let x = cur_vals[i];
                while j < prev_vals.len() && prev_vals[j] <= x {
                    prefix += dp[j];
                    if prefix >= MOD {
                        prefix -= MOD;
                    }
                    j += 1;
                }
                next[i] = prefix;
            }
            prev_vals = cur_vals.clone();
            dp = next;
        }
        let mut ans = 0;
        for x in dp {
            ans += x;
            if ans >= MOD {
                ans -= MOD;
            }
        }
        ans
    }
}
