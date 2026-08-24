// LeetCode 0947 - Most Stones Removed with Same Row or Column
// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn remove_stones(stones: Vec<Vec<i32>>) -> i32 {
        let mut parent = HashMap::new();
        fn find(parent: &mut HashMap<i32, i32>, x: i32) -> i32 {
            parent.entry(x).or_insert(x);
            if parent[&x] != x {
                let p = find(parent, parent[&x]);
                parent.insert(x, p);
            }
            parent[&x]
        }
        for s in &stones {
            let a = find(&mut parent, s[0]);
            let b = find(&mut parent, !s[1]);
            parent.insert(a, b);
        }
        let mut roots = HashSet::new();
        for s in &stones {
            roots.insert(find(&mut parent, s[0]));
        }
        stones.len() as i32 - roots.len() as i32
    }
}
