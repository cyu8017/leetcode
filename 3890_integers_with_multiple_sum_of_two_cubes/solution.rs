// LeetCode 3890 - Integers With Multiple Sum of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

use std::collections::HashMap;

impl Solution {
    pub fn find_good_integers(n: i32) -> Vec<i32> {
        const LIMIT: i64 = 1_000_000_000;
        let mut cnt = HashMap::new();
        let cubes: Vec<i64> = (0..=1000).map(|i| i as i64 * i as i64 * i as i64).collect();
        for a in 1..=1000 {
            for b in a..=1000 {
                let x = cubes[a] + cubes[b];
                if x > LIMIT {
                    break;
                }
                *cnt.entry(x as i32).or_insert(0) += 1;
            }
        }
        let mut good: Vec<i32> = cnt.into_iter().filter(|(_, v)| *v > 1).map(|(x, _)| x).collect();
        good.sort_unstable();
        let pos = good.partition_point(|&x| x <= n);
        good[..pos].to_vec()
    }
}
