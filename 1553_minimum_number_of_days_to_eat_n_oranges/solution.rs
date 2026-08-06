// LeetCode 1553 - Minimum Number of Days to Eat N Oranges
// https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/

use std::collections::HashMap;

impl Solution {
    pub fn min_days(n: i32) -> i32 {
        fn dp(x: i32, memo: &mut HashMap<i32, i32>) -> i32 {
            if x <= 1 {
                return x;
            }
            if let Some(&v) = memo.get(&x) {
                return v;
            }
            let v = 1 + (x % 2 + dp(x / 2, memo)).min(x % 3 + dp(x / 3, memo));
            memo.insert(x, v);
            v
        }
        dp(n, &mut HashMap::new())
    }
}
