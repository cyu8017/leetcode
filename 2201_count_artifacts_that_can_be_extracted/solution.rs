// LeetCode 2201 - Count Artifacts That Can Be Extracted
// https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

use std::collections::HashSet;

impl Solution {
    pub fn dig_artifacts(n: i32, artifacts: Vec<Vec<i32>>, dig: Vec<Vec<i32>>) -> i32 {
        let _ = n;
        let dug: HashSet<(i32, i32)> = dig.into_iter().map(|d| (d[0], d[1])).collect();
        let mut ans = 0;
        for a in artifacts {
            let mut ok = true;
            for r in a[0]..=a[2] {
                for c in a[1]..=a[3] {
                    if !dug.contains(&(r, c)) {
                        ok = false;
                    }
                }
            }
            if ok {
                ans += 1;
            }
        }
        ans
    }
}
