// LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

use std::collections::HashSet;

impl Solution {
    pub fn maximize_square_area(m: i32, n: i32, h_fences: Vec<i32>, v_fences: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn gaps(mut fences: Vec<i32>, bound: i32) -> HashSet<i32> {
            fences.push(1);
            fences.push(bound);
            fences.sort_unstable();
            let mut g = HashSet::new();
            for i in 0..fences.len() {
                for j in (i + 1)..fences.len() {
                    g.insert(fences[j] - fences[i]);
                }
            }
            g
        }
        let hg = gaps(h_fences, m);
        let vg = gaps(v_fences, n);
        let mut best = -1i64;
        for &g in &hg {
            if vg.contains(&g) && g as i64 > best {
                best = g as i64;
            }
        }
        if best < 0 {
            return -1;
        }
        (best * best % MOD) as i32
    }
}
