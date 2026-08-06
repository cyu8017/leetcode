// LeetCode 1925 - Count Square Sum Triples
// https://leetcode.com/problems/count-square-sum-triples/

use std::collections::HashSet;

impl Solution {
    pub fn count_triples(n: i32) -> i32 {
        let squares: HashSet<i32> = (1..=n).map(|i| i * i).collect();
        let mut ans = 0;
        for a in 1..=n {
            for b in 1..=n {
                if squares.contains(&(a * a + b * b)) {
                    ans += 1;
                }
            }
        }
        ans
    }
}
