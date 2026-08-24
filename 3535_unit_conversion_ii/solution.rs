// LeetCode 3535 - Unit Conversion II
// https://leetcode.com/problems/unit-conversion-ii/

impl Solution {
    const MOD: i64 = 1_000_000_007;

    fn qpow(mut x: i64, mut n: i32) -> i64 {
        let mut res = 1i64;
        while n > 0 {
            if n & 1 == 1 {
                res = res * x % Self::MOD;
            }
            x = x * x % Self::MOD;
            n >>= 1;
        }
        res
    }

    pub fn query_conversions(conversions: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = conversions.len() + 1;
        let mut g = vec![Vec::<(usize, i32)>::new(); n];
        for e in &conversions {
            g[e[0] as usize].push((e[1] as usize, e[2]));
        }
        let mut res = vec![0i32; n];
        fn dfs(s: usize, mul: i32, g: &[Vec<(usize, i32)>], res: &mut [i32]) {
            res[s] = mul;
            for &(t, w) in &g[s] {
                dfs(t, ((mul as i64 * w as i64) % Solution::MOD) as i32, g, res);
            }
        }
        dfs(0, 1, &g, &mut res);
        queries
            .iter()
            .map(|q| ((res[q[1] as usize] as i64 * Self::qpow(res[q[0] as usize] as i64, Self::MOD as i32 - 2)) % Self::MOD) as i32)
            .collect()
    }
}
