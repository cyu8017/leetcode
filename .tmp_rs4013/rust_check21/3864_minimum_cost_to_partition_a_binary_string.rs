struct Solution;
// LeetCode 3864 - Minimum Cost to Partition a Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

impl Solution {
    pub fn min_cost(s: String, enc_cost: i32, flat_cost: i32) -> i64 {
        let n = s.len();
        let b = s.as_bytes();
        let mut pre = vec![0; n + 1];
        for i in 1..=n {
            pre[i] = pre[i - 1] + (b[i - 1] - b'0') as i32;
        }
        fn dfs(l: usize, r: usize, pre: &[i32], enc_cost: i32, flat_cost: i32) -> i64 {
            let x = pre[r] - pre[l];
            let mut res = if x != 0 {
                (r - l) as i64 * x as i64 * enc_cost as i64
            } else {
                flat_cost as i64
            };
            if (r - l) % 2 == 0 {
                let m = (l + r) / 2;
                res = res.min(dfs(l, m, pre, enc_cost, flat_cost) + dfs(m, r, pre, enc_cost, flat_cost));
            }
            res
        }
        dfs(0, n, &pre, enc_cost, flat_cost)
    }
}
