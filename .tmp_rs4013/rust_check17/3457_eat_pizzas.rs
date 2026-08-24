struct Solution;
// LeetCode 3457 - Eat Pizzas!
// https://leetcode.com/problems/eat-pizzas/

impl Solution {
    pub fn max_weight(mut pizzas: Vec<i32>) -> i64 {
        pizzas.sort_unstable();
        let n = pizzas.len();
        let days = n / 4;
        let mut ans = 0i64;
        let odd_days = (days + 1) / 2;
        let even_days = days / 2;
        let mut idx = n as i32 - 1;
        for _ in 0..odd_days {
            ans += pizzas[idx as usize] as i64;
            idx -= 1;
        }
        for _ in 0..even_days {
            idx -= 1;
            ans += pizzas[idx as usize] as i64;
            idx -= 1;
        }
        ans
    }
}

fn main() {}
