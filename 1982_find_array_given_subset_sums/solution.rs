// LeetCode 1982 - Find Array Given Subset Sums
// https://leetcode.com/problems/find-array-given-subset-sums/

use std::collections::HashMap;

impl Solution {
    pub fn recover_array(n: i32, mut sums: Vec<i32>) -> Vec<i32> {
        sums.sort_unstable();
        let mut ans = Vec::new();
        for _ in 0..n {
            let d = sums[1] - sums[0];
            let mut count: HashMap<i32, i32> = HashMap::new();
            for &x in &sums {
                *count.entry(x).or_insert(0) += 1;
            }
            let mut without = Vec::new();
            let mut with_d = Vec::new();
            for &x in &sums {
                if count.get(&x).copied().unwrap_or(0) == 0 {
                    continue;
                }
                *count.get_mut(&x).unwrap() -= 1;
                *count.entry(x + d).or_insert(0) -= 1;
                without.push(x);
                with_d.push(x + d);
            }
            if without.contains(&0) {
                ans.push(d);
                sums = without;
            } else {
                ans.push(-d);
                sums = with_d;
            }
        }
        ans
    }
}
