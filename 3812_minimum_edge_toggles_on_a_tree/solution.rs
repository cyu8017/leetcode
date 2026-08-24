// LeetCode 3812 - Minimum Edge Toggles On A Tree
// https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/

impl Solution {
    pub fn minimum_flips(
        n: i32,
        edges: Vec<Vec<i32>>,
        start: String,
        target: String,
    ) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for i in 0..n.saturating_sub(1) {
            let a = edges[i][0] as usize;
            let b = edges[i][1] as usize;
            g[a].push((b, i as i32));
            g[b].push((a, i as i32));
        }
        let start = start.into_bytes();
        let target = target.into_bytes();
        let mut ans = Vec::new();

        fn dfs(
            a: usize,
            fa: i32,
            g: &[Vec<(usize, i32)>],
            start: &[u8],
            target: &[u8],
            ans: &mut Vec<i32>,
        ) -> bool {
            let mut rev = start[a] != target[a];
            for &(b, i) in &g[a] {
                if b as i32 != fa && dfs(b, a as i32, g, start, target, ans) {
                    ans.push(i);
                    rev = !rev;
                }
            }
            rev
        }

        if dfs(0, -1, &g, &start, &target, &mut ans) {
            return vec![-1];
        }
        ans.sort_unstable();
        ans
    }
}
