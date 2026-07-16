// LeetCode 0256 - Paint House
// https://leetcode.com/problems/paint-house/

impl Solution {
    pub fn min_cost(costs: Vec<Vec<i32>>) -> i32 {
        if costs.is_empty() {
            return 0;
        }
        let mut previous = costs[0].clone();
        for row in 1..costs.len() {
            previous = vec![
                costs[row][0] + previous[1].min(previous[2]),
                costs[row][1] + previous[0].min(previous[2]),
                costs[row][2] + previous[0].min(previous[1]),
            ];
        }
        previous.into_iter().min().unwrap()
    }
}
