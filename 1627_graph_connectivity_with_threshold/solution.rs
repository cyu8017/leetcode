// LeetCode 1627 - Graph Connectivity With Threshold
// https://leetcode.com/problems/graph-connectivity-with-threshold/

impl Solution {
    pub fn are_connected(n: i32, threshold: i32, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n = n as usize;
        let mut parent: Vec<usize> = (0..=n).collect();
        let find = |parent: &mut Vec<usize>, mut x: usize| -> usize {
            while x != parent[x] {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        };
        for d in (threshold as usize + 1)..=n {
            let mut x = 2 * d;
            while x <= n {
                let a = find(&mut parent, d);
                let b = find(&mut parent, x);
                if a != b {
                    parent[b] = a;
                }
                x += d;
            }
        }
        queries
            .into_iter()
            .map(|q| find(&mut parent, q[0] as usize) == find(&mut parent, q[1] as usize))
            .collect()
    }
}
