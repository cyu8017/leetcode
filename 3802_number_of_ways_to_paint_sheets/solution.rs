// LeetCode 3802 - Number of Ways to Paint Sheets
// https://leetcode.com/problems/number-of-ways-to-paint-sheets/

impl Solution {
    pub fn number_of_ways(n: i32, mut limit: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        limit.sort_unstable();
        let mut points = vec![1, n];
        for &x in &limit {
            if x + 1 > 1 && x + 1 < n {
                points.push(x + 1);
            }
            if n - x > 1 && n - x < n {
                points.push(n - x);
            }
        }
        points.sort_unstable();
        points.dedup();
        let count_ge = |x: i32| -> i64 { (limit.len() - limit.partition_point(|&v| v < x)) as i64 };
        let mut ans = 0i64;
        for i in 0..points.len().saturating_sub(1) {
            let x = points[i];
            let a = count_ge(x);
            let b = count_ge(n - x);
            let same = count_ge(x.max(n - x));
            let ways = (a * b - same) % MOD;
            let length = (points[i + 1] - x) as i64;
            ans = (ans + ways * length) % MOD;
        }
        if ans < 0 {
            ans += MOD;
        }
        ans as i32
    }
}
