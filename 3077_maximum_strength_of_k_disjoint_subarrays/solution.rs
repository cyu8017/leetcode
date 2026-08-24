// LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
// https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

impl Solution {
    pub fn maximum_strength(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let k = k as usize;
        let inf = i64::MIN / 2;
        let mut f = vec![vec![vec![inf; 2]; k + 1]; n + 1];
        f[0][0][0] = 0;
        for i in 1..=n {
            let x = nums[i - 1] as i64;
            for j in 0..=k {
                let sign = if j & 1 == 1 { 1i64 } else { -1i64 };
                let val = sign * x * (k as i64 - j as i64 + 1);
                f[i][j][0] = f[i - 1][j][0].max(f[i - 1][j][1]);
                f[i][j][1] = f[i][j][1].max(f[i - 1][j][1].saturating_add(val));
                if j > 0 {
                    let t = f[i - 1][j - 1][0].max(f[i - 1][j - 1][1]).saturating_add(val);
                    f[i][j][1] = f[i][j][1].max(t);
                }
            }
        }
        f[n][k][0].max(f[n][k][1])
    }
}
