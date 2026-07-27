// LeetCode 1648 - Sell Diminishing-Valued Colored Balls
// https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

impl Solution {
    pub fn max_profit(mut inventory: Vec<i32>, mut orders: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        inventory.sort_unstable_by(|a, b| b.cmp(a));
        inventory.push(0);
        let mut ans = 0i64;
        for i in 0..inventory.len() - 1 {
            let width = (i + 1) as i64;
            let high = inventory[i] as i64;
            let low = inventory[i + 1] as i64;
            let balls = width * (high - low);
            let take = balls.min(orders as i64);
            let full = take / width;
            let rem = take % width;
            let bottom = high - full;
            ans = (ans
                + width * (high + bottom + 1) * full / 2 % MOD
                + rem * bottom % MOD)
                % MOD;
            orders -= take as i32;
            if orders == 0 {
                break;
            }
        }
        ans as i32
    }
}
