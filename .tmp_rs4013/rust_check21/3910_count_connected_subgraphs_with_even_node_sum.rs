struct Solution;
// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

impl Solution {
    pub fn even_sum_subgraphs(nums: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let m = (1 << n) - 1;
        let mut ans = 0;
        fn dfs(u: usize, vis: &mut i32, g: &[Vec<usize>]) {
            *vis |= 1 << u;
            for &v in &g[u] {
                if ((*vis >> v) & 1) == 0 {
                    dfs(v, vis, g);
                }
            }
        }
        for sub in 1..=m {
            let mut s = 0;
            for i in 0..n {
                if (sub >> i) & 1 == 1 {
                    s += nums[i];
                }
            }
            if s % 2 != 0 {
                continue;
            }
            let mut vis = m ^ sub;
            let start = 31 - (sub as u32).leading_zeros();
            dfs(start as usize, &mut vis, &g);
            if vis == m {
                ans += 1;
            }
        }
        ans
    }
}
