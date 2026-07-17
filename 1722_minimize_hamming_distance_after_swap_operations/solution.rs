// LeetCode 1722 - Minimize Hamming Distance After Swap Operations
// https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_hamming_distance(
        source: Vec<i32>,
        target: Vec<i32>,
        allowed_swaps: Vec<Vec<i32>>,
    ) -> i32 {
        fn find(parent: &mut Vec<usize>, mut x: usize) -> usize {
            while parent[x] != x {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }

        let n = source.len();
        let mut parent: Vec<usize> = (0..n).collect();
        for swap in &allowed_swaps {
            let ra = find(&mut parent, swap[0] as usize);
            let rb = find(&mut parent, swap[1] as usize);
            if ra != rb {
                parent[rb] = ra;
            }
        }
        let mut groups: HashMap<usize, HashMap<i32, i32>> = HashMap::new();
        for (i, &value) in source.iter().enumerate() {
            let root = find(&mut parent, i);
            *groups.entry(root).or_default().entry(value).or_insert(0) += 1;
        }
        let mut ans = 0;
        for (i, &value) in target.iter().enumerate() {
            let root = find(&mut parent, i);
            let counts = groups.get_mut(&root).unwrap();
            let remaining = counts.entry(value).or_insert(0);
            if *remaining > 0 {
                *remaining -= 1;
            } else {
                ans += 1;
            }
        }
        ans
    }
}
