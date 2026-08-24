// LeetCode 3786 - Total Sum of Interaction Cost in Tree Groups
// https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

impl Solution {
    pub fn interaction_cost(n: i32, edges: Vec<Vec<i32>>, group: Vec<i32>) -> i64 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut total = [0i32; 21];
        for &x in &group {
            total[x as usize] += 1;
        }
        let mut parent = vec![-2i32; n];
        parent[0] = -1;
        let mut order = vec![0usize];
        let mut i = 0;
        while i < order.len() {
            let u = order[i];
            for &v in &g[u] {
                if parent[v] == -2 {
                    parent[v] = u as i32;
                    order.push(v);
                }
            }
            i += 1;
        }
        let mut count = vec![[0i32; 21]; n];
        let mut ans = 0i64;
        for i in (0..n).rev() {
            let u = order[i];
            count[u][group[u] as usize] += 1;
            for &v in &g[u] {
                if parent[v] != u as i32 {
                    continue;
                }
                for c in 1..=20 {
                    let x = count[v][c];
                    ans += x as i64 * (total[c] - x) as i64;
                    count[u][c] += x;
                }
            }
        }
        ans
    }
}
