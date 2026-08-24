// LeetCode 3669 - Balanced K-Factor Decomposition
// https://leetcode.com/problems/balanced-k-factor-decomposition/

impl Solution {
    pub fn min_difference(n: i32, k: i32) -> Vec<i32> {
        const MX: usize = 100001;
        let mut g = vec![Vec::new(); MX];
        for i in 1..MX {
            let mut j = i;
            while j < MX {
                g[j].push(i as i32);
                j += i;
            }
        }
        let k = k as usize;
        let mut cur = i32::MAX;
        let mut ans = Vec::new();
        let mut path = vec![0; k];
        fn dfs(
            i: usize,
            x: i32,
            mi: i32,
            mx: i32,
            g: &[Vec<i32>],
            path: &mut [i32],
            cur: &mut i32,
            ans: &mut Vec<i32>,
        ) {
            if i == 0 {
                let d = mx.max(x) - mi.min(x);
                if d < *cur {
                    *cur = d;
                    path[i] = x;
                    *ans = path.to_vec();
                }
                return;
            }
            for &y in &g[x as usize] {
                path[i] = y;
                dfs(i - 1, x / y, mi.min(y), mx.max(y), g, path, cur, ans);
            }
        }
        dfs(k - 1, n, i32::MAX, 0, &g, &mut path, &mut cur, &mut ans);
        ans
    }
}
