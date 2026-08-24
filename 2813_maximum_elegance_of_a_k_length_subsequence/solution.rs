// LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

use std::collections::HashSet;

impl Solution {
    pub fn find_maximum_elegance(mut items: Vec<Vec<i32>>, k: i32) -> i64 {
        items.sort_unstable_by(|a, b| b[0].cmp(&a[0]));
        let k = k as usize;
        let mut seen = HashSet::new();
        let mut total = 0i64;
        let mut dup = Vec::new();
        for i in 0..k {
            total += items[i][0] as i64;
            let c = items[i][1];
            if seen.contains(&c) {
                dup.push(items[i][0]);
            } else {
                seen.insert(c);
            }
        }
        let mut ans = total + seen.len() as i64 * seen.len() as i64;
        for i in k..items.len() {
            let c = items[i][1];
            if seen.contains(&c) || dup.is_empty() {
                continue;
            }
            total += items[i][0] as i64 - dup.pop().unwrap() as i64;
            seen.insert(c);
            ans = ans.max(total + seen.len() as i64 * seen.len() as i64);
        }
        ans
    }
}
