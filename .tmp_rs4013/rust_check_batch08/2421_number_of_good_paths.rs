struct Solution;
// LeetCode 2421 - Number of Good Paths
// https://leetcode.com/problems/number-of-good-paths/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_good_paths(vals: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = vals.len();
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        let mut parent: Vec<usize> = (0..n).collect();
        let mut size = vec![1i32; n];
        fn find(parent: &mut [usize], x: usize) -> usize {
            if parent[x] != x {
                parent[x] = find(parent, parent[x]);
            }
            parent[x]
        }
        let mut nodes: Vec<usize> = (0..n).collect();
        nodes.sort_by_key(|&i| vals[i]);
        let mut ans = n as i32;
        let mut i = 0;
        while i < n {
            let mut j = i;
            while j < n && vals[nodes[j]] == vals[nodes[i]] {
                j += 1;
            }
            for k in i..j {
                let u = nodes[k];
                for &v in &g[u] {
                    if vals[v] <= vals[u] {
                        let ru = find(&mut parent, u);
                        let rv = find(&mut parent, v);
                        if ru != rv {
                            parent[ru] = rv;
                            size[rv] += size[ru];
                        }
                    }
                }
            }
            let mut freq: HashMap<usize, i32> = HashMap::new();
            for k in i..j {
                let r = find(&mut parent, nodes[k]);
                *freq.entry(r).or_insert(0) += 1;
            }
            for &c in freq.values() {
                ans += c * (c - 1) / 2;
            }
            i = j;
        }
        ans
    }
}

fn main() {}
