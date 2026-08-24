// LeetCode 3728 - Stable Subarrays With Equal Boundary and Interior Sum
// https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

use std::collections::HashMap;

impl Solution {
    pub fn count_stable_subarrays(capacity: Vec<i32>) -> i64 {
        let n = capacity.len();
        let mut s = vec![0i64; n + 1];
        for i in 1..=n {
            s[i] = s[i - 1] + capacity[i - 1] as i64;
        }
        let mut cnt: HashMap<(i32, i64), i32> = HashMap::new();
        let mut ans = 0i64;
        for r in 2..n {
            let l = r - 2;
            *cnt.entry((capacity[l], capacity[l] as i64 + s[l + 1])).or_insert(0) += 1;
            ans += *cnt.get(&(capacity[r], s[r])).unwrap_or(&0) as i64;
        }
        ans
    }
}
