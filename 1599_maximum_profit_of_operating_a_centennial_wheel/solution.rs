// LeetCode 1599 - Maximum Profit of Operating a Centennial Wheel
// https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

impl Solution {
    pub fn min_operations_max_profit(
        customers: Vec<i32>,
        boarding_cost: i32,
        running_cost: i32,
    ) -> i32 {
        let mut waiting = 0;
        let mut profit = 0;
        let mut best = 0;
        let mut answer = 0;
        let mut rotation = 0;
        let mut i = 0;
        while i < customers.len() || waiting > 0 {
            if i < customers.len() {
                waiting += customers[i];
            }
            let boarded = waiting.min(4);
            waiting -= boarded;
            rotation += 1;
            profit += boarded * boarding_cost - running_cost;
            if profit > best {
                best = profit;
                answer = rotation;
            }
            i += 1;
        }
        if best > 0 {
            answer
        } else {
            -1
        }
    }
}
