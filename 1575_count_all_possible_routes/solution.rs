// LeetCode 1575 - Count All Possible Routes
// https://leetcode.com/problems/count-all-possible-routes/

use std::collections::HashMap;

impl Solution {
    pub fn count_routes(locations: Vec<i32>, start: i32, finish: i32, fuel: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut memo = HashMap::new();
        fn dp(
            city: usize,
            left: i32,
            locations: &[i32],
            finish: usize,
            memo: &mut HashMap<(usize, i32), i64>,
        ) -> i64 {
            if let Some(&v) = memo.get(&(city, left)) {
                return v;
            }
            let mut total = if city == finish { 1 } else { 0 };
            for nxt in 0..locations.len() {
                let cost = (locations[city] - locations[nxt]).abs();
                if nxt != city && cost <= left {
                    total += dp(nxt, left - cost, locations, finish, memo);
                }
            }
            total %= MOD;
            memo.insert((city, left), total);
            total
        }
        dp(start as usize, fuel, &locations, finish as usize, &mut memo) as i32
    }
}
