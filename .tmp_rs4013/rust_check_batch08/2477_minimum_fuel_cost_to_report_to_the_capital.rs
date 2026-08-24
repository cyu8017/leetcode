struct Solution;
// LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

impl Solution {
    pub fn minimum_fuel_cost(roads: Vec<Vec<i32>>, seats: i32) -> i64 {
        let n = roads.len() + 1;
        let mut g = vec![Vec::new(); n];
        for r in &roads {
            let (a, b) = (r[0] as usize, r[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        let mut ans = 0i64;
        fn dfs(u: usize, p: i32, seats: i32, g: &[Vec<usize>], ans: &mut i64) -> i32 {
            let mut people = 1;
            for &v in &g[u] {
                if v as i32 != p {
                    people += dfs(v, u as i32, seats, g, ans);
                }
            }
            if u != 0 {
                *ans += ((people + seats - 1) / seats) as i64;
            }
            people
        }
        dfs(0, -1, seats, &g, &mut ans);
        ans
    }
}

fn main() {}
