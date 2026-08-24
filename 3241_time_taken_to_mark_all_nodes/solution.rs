// LeetCode 3241 - Time Taken to Mark All Nodes
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/

impl Solution {
    pub fn time_taken(edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = edges.len() + 1;
        let mut ans = vec![0; n];
        let mut tree = vec![Vec::new(); n];
        let mut dp = vec![[(0, 0), (0, 0)]; n];
        for e in &edges {
            tree[e[0] as usize].push(e[1] as usize);
            tree[e[1] as usize].push(e[0] as usize);
        }
        let get_time = |u: usize| if u % 2 == 0 { 2 } else { 1 };
        fn dfs(u: usize, prev: i32, tree: &[Vec<usize>], dp: &mut [([(i32, i32); 2])]) -> i32 {
            let mut t1 = (0, 0);
            let mut t2 = (0, 0);
            for &v in &tree[u] {
                if v as i32 == prev {
                    continue;
                }
                let t = dfs(v, u as i32, tree, dp) + if v % 2 == 0 { 2 } else { 1 };
                if t >= t1.1 {
                    t2 = t1;
                    t1 = (v as i32, t);
                } else if t > t2.1 {
                    t2 = (v as i32, t);
                }
            }
            dp[u] = [t1, t2];
            t1.1
        }
        fn reroot(
            u: usize,
            prev: i32,
            max_time: i32,
            tree: &[Vec<usize>],
            dp: &[[(i32, i32); 2]],
            ans: &mut [i32],
        ) {
            ans[u] = max_time.max(dp[u][0].1);
            for &v in &tree[u] {
                if v as i32 == prev {
                    continue;
                }
                let side = if dp[u][0].0 == v as i32 { dp[u][1].1 } else { dp[u][0].1 };
                let new_max = max_time.max(side);
                let gt = if u % 2 == 0 { 2 } else { 1 };
                reroot(v, u as i32, gt + new_max, tree, dp, ans);
            }
        }
        dfs(0, -1, &tree, &mut dp);
        reroot(0, -1, 0, &tree, &dp, &mut ans);
        let _ = get_time;
        ans
    }
}
