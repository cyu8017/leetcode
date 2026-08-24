struct Solution;
// LeetCode 3203 - Find Minimum Diameter After Merging Two Trees
// https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

impl Solution {
    fn tree_diameter(edges: &[Vec<i32>]) -> i32 {
        let n = edges.len() + 1;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut ans = 0;
        let mut a = 0;
        fn dfs(i: usize, fa: i32, t: i32, g: &[Vec<usize>], ans: &mut i32, a: &mut usize) {
            for &j in &g[i] {
                if j as i32 != fa {
                    dfs(j, i as i32, t + 1, g, ans, a);
                }
            }
            if *ans < t {
                *ans = t;
                *a = i;
            }
        }
        dfs(0, -1, 0, &g, &mut ans, &mut a);
        dfs(a, -1, 0, &g, &mut ans, &mut a);
        ans
    }

    pub fn minimum_diameter_after_merge(edges1: Vec<Vec<i32>>, edges2: Vec<Vec<i32>>) -> i32 {
        let d1 = Self::tree_diameter(&edges1);
        let d2 = Self::tree_diameter(&edges2);
        d1.max(d2).max((d1 + 1) / 2 + (d2 + 1) / 2 + 1)
    }
}

fn main() {}
