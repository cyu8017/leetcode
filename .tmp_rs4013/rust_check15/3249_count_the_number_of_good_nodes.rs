struct Solution;
// LeetCode 3249 - Count the Number of Good Nodes
// https://leetcode.com/problems/count-the-number-of-good-nodes/

impl Solution {
    pub fn count_good_nodes(edges: Vec<Vec<i32>>) -> i32 {
        let n = edges.len() + 1;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut ans = 0;
        fn dfs(a: usize, fa: i32, g: &[Vec<usize>], ans: &mut i32) -> i32 {
            let mut pre = -1;
            let mut cnt = 1;
            let mut ok = 1;
            for &b in &g[a] {
                if b as i32 != fa {
                    let cur = dfs(b, a as i32, g, ans);
                    cnt += cur;
                    if pre < 0 {
                        pre = cur;
                    } else if pre != cur {
                        ok = 0;
                    }
                }
            }
            *ans += ok;
            cnt
        }
        dfs(0, -1, &g, &mut ans);
        ans
    }
}

fn main() {}
