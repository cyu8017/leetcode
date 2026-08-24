// LeetCode 3756 - Concatenate Non Zero Digits And Multiply By Sum Ii
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

impl Solution {
    pub fn sum_and_multiply(s: String, queries: Vec<Vec<i32>>) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;
        const MX: usize = 100001;
        let pw: Vec<i64> = {
            let mut p = vec![0i64; MX];
            p[0] = 1;
            for i in 1..MX {
                p[i] = p[i - 1] * 10 % MOD;
            }
            p
        };
        let n = s.len();
        let bytes = s.as_bytes();
        let mut sum_d = vec![0i32; n + 1];
        let mut cnt_n0 = vec![0i32; n + 1];
        let mut p = vec![0i64; n + 1];
        for i in 1..=n {
            let d = (bytes[i - 1] - b'0') as i64;
            sum_d[i] = sum_d[i - 1] + d as i32;
            cnt_n0[i] = cnt_n0[i - 1];
            if d > 0 {
                cnt_n0[i] += 1;
                p[i] = (p[i - 1] * 10 + d) % MOD;
            } else {
                p[i] = p[i - 1];
            }
        }
        let mut ans = vec![0i32; queries.len()];
        for (i, q) in queries.iter().enumerate() {
            let l = q[0] as usize;
            let r = q[1] as usize;
            let n0 = (cnt_n0[r + 1] - cnt_n0[l]) as usize;
            let sd = (sum_d[r + 1] - sum_d[l]) as i64;
            let x = (p[r + 1] - p[l] * pw[n0] % MOD + MOD) % MOD;
            ans[i] = (x * sd % MOD) as i32;
        }
        ans
    }
}
