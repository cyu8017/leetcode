// LeetCode 3493 - Properties Graph
// https://leetcode.com/problems/properties-graph/

use std::collections::HashSet;

impl Solution {
    pub fn number_of_components(properties: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = properties.len();
        let sets: Vec<HashSet<i32>> = properties
            .iter()
            .map(|p| p.iter().copied().collect())
            .collect();
        let mut parent: Vec<usize> = (0..n).collect();
        fn find(parent: &mut [usize], x: usize) -> usize {
            if parent[x] != x {
                parent[x] = find(parent, parent[x]);
            }
            parent[x]
        }
        let mut unite = |parent: &mut [usize], a: usize, b: usize| {
            let ra = find(parent, a);
            let rb = find(parent, b);
            if ra != rb {
                parent[ra] = rb;
            }
        };
        for i in 0..n {
            for j in (i + 1)..n {
                let cnt = sets[i].iter().filter(|v| sets[j].contains(v)).count() as i32;
                if cnt >= k {
                    unite(&mut parent, i, j);
                }
            }
        }
        let mut comp = HashSet::new();
        for i in 0..n {
            comp.insert(find(&mut parent, i));
        }
        comp.len() as i32
    }
}
