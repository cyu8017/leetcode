// LeetCode 3965 - Finish Time Of Tasks I
// https://leetcode.com/problems/finish-time-of-tasks-i/

impl Solution {
    pub fn finish_time(n: i32, edges: Vec<Vec<i32>>, base_time: Vec<i32>) -> i64 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
        }
        fn dfs(i: usize, g: &[Vec<usize>], base_time: &[i32]) -> i64 {
            if g[i].is_empty() {
                return base_time[i] as i64;
            }
            const INF: i64 = 1 << 62;
            let mut earliest = INF;
            let mut latest = -INF;
            for &j in &g[i] {
                let a = dfs(j, g, base_time);
                earliest = earliest.min(a);
                latest = latest.max(a);
            }
            let own_duration = (latest - earliest) + base_time[i] as i64;
            latest + own_duration
        }
        dfs(0, &g, &base_time)
    }
}
