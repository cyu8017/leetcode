// LeetCode 1774 - Closest Dessert Cost
// https://leetcode.com/problems/closest-dessert-cost/

impl Solution {
    pub fn closest_cost(base_costs: Vec<i32>, topping_costs: Vec<i32>, target: i32) -> i32 {
        fn dfs(i: usize, cur: i32, target: i32, toppings: &[i32], best: &mut i32) {
            let cur_diff = (cur - target).abs();
            let best_diff = (*best - target).abs();
            if cur_diff < best_diff || (cur_diff == best_diff && cur < *best) {
                *best = cur;
            }
            if i == toppings.len() || cur >= target {
                return;
            }
            dfs(i + 1, cur, target, toppings, best);
            dfs(i + 1, cur + toppings[i], target, toppings, best);
            dfs(i + 1, cur + 2 * toppings[i], target, toppings, best);
        }

        let mut best = 1 << 29;
        for &base in &base_costs {
            dfs(0, base, target, &topping_costs, &mut best);
        }
        best
    }
}
