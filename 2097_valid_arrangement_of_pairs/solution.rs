// LeetCode 2097 - Valid Arrangement of Pairs
// https://leetcode.com/problems/valid-arrangement-of-pairs/

use std::collections::HashMap;

impl Solution {
    pub fn valid_arrangement(pairs: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut g: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut indeg: HashMap<i32, i32> = HashMap::new();
        let mut outdeg: HashMap<i32, i32> = HashMap::new();
        for p in &pairs {
            let (u, v) = (p[0], p[1]);
            g.entry(u).or_default().push(v);
            *outdeg.entry(u).or_default() += 1;
            *indeg.entry(v).or_default() += 1;
        }
        let mut start = pairs[0][0];
        for (&u, &o) in &outdeg {
            if o - indeg.get(&u).copied().unwrap_or(0) == 1 {
                start = u;
                break;
            }
        }
        let mut path = Vec::new();
        fn dfs(u: i32, g: &mut HashMap<i32, Vec<i32>>, path: &mut Vec<i32>) {
            while let Some(v) = g.get_mut(&u).and_then(|adj| adj.pop()) {
                dfs(v, g, path);
            }
            path.push(u);
        }
        dfs(start, &mut g, &mut path);
        path.reverse();
        path.windows(2).map(|w| vec![w[0], w[1]]).collect()
    }
}
