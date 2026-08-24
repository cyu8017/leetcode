// LeetCode 2322 - Minimum Score After Removals on a Tree
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

impl Solution {
    pub fn minimum_score(nums: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut xorv = vec![0i32; n];
        let mut in_t = vec![0i32; n];
        let mut out_t = vec![0i32; n];
        fn dfs(
            u: usize,
            p: i32,
            g: &[Vec<usize>],
            nums: &[i32],
            xorv: &mut [i32],
            in_t: &mut [i32],
            out_t: &mut [i32],
            time: &mut i32,
        ) {
            in_t[u] = *time;
            *time += 1;
            xorv[u] = nums[u];
            for &v in &g[u] {
                if v as i32 != p {
                    dfs(v, u as i32, g, nums, xorv, in_t, out_t, time);
                    xorv[u] ^= xorv[v];
                }
            }
            out_t[u] = *time;
        }
        dfs(0, -1, &g, &nums, &mut xorv, &mut in_t, &mut out_t, &mut 0);
        let is_ancestor = |a: usize, b: usize| in_t[a] <= in_t[b] && out_t[b] <= out_t[a];
        let total = xorv[0];
        let mut ans = i32::MAX;
        for i in 1..n {
            for j in i + 1..n {
                let (a, b, c) = if is_ancestor(i, j) {
                    (xorv[j], xorv[i] ^ xorv[j], total ^ xorv[i])
                } else if is_ancestor(j, i) {
                    (xorv[i], xorv[j] ^ xorv[i], total ^ xorv[j])
                } else {
                    (xorv[i], xorv[j], total ^ xorv[i] ^ xorv[j])
                };
                ans = ans.min(a.max(b).max(c) - a.min(b).min(c));
            }
        }
        ans
    }
}
