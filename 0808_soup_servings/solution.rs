// LeetCode 0808 - Soup Servings
// https://leetcode.com/problems/soup-servings/

use std::collections::HashMap;

impl Solution {
    pub fn soup_servings(n: i32) -> f64 {
        if n >= 4800 {
            return 1.0;
        }
        let units = (n + 24) / 25;
        let mut memo = HashMap::new();
        Self::dp(units, units, &mut memo)
    }

    fn dp(a: i32, b: i32, memo: &mut HashMap<i64, f64>) -> f64 {
        if a <= 0 && b <= 0 {
            return 0.5;
        }
        if a <= 0 {
            return 1.0;
        }
        if b <= 0 {
            return 0.0;
        }
        let key = ((a as i64) << 16) | (b as i64);
        if let Some(&val) = memo.get(&key) {
            return val;
        }
        let val = 0.25
            * (Self::dp(a - 4, b, memo)
                + Self::dp(a - 3, b - 1, memo)
                + Self::dp(a - 2, b - 2, memo)
                + Self::dp(a - 1, b - 3, memo));
        memo.insert(key, val);
        val
    }
}
