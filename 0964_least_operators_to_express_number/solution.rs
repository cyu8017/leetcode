// LeetCode 0964 - Least Operators to Express Number
// https://leetcode.com/problems/least-operators-to-express-number/

use std::collections::HashMap;

impl Solution {
    pub fn least_ops_express_target(x: i32, target: i32) -> i32 {
        fn dfs(x: i32, t: i32, memo: &mut HashMap<i32, i32>) -> i32 {
            if let Some(&v) = memo.get(&t) {
                return v;
            }
            if x > t {
                let v = (2 * t - 1).min(2 * (x - t));
                memo.insert(t, v);
                return v;
            }
            if x == t {
                memo.insert(t, 0);
                return 0;
            }
            let mut prod = x as i64;
            let mut n = 0;
            while prod < t as i64 {
                prod *= x as i64;
                n += 1;
            }
            if prod == t as i64 {
                memo.insert(t, n);
                return n;
            }
            let mut ans = dfs(x, t - (prod / x as i64) as i32, memo) + n;
            if prod < 2 * t as i64 {
                ans = ans.min(dfs(x, prod as i32 - t, memo) + n + 1);
            }
            memo.insert(t, ans);
            ans
        }
        let mut memo = HashMap::new();
        dfs(x, target, &mut memo)
    }
}
