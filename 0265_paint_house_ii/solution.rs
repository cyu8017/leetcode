// LeetCode 0265 - Paint House II
// https://leetcode.com/problems/paint-house-ii/

impl Solution {
    pub fn min_cost_ii(costs: Vec<Vec<i32>>) -> i32 {
        if costs.is_empty() {
            return 0;
        }
        let color_count = costs[0].len();
        let mut previous = costs[0].clone();
        for row in 1..costs.len() {
            let min_cost = *previous.iter().min().unwrap();
            let min_index = previous.iter().position(|&value| value == min_cost).unwrap();
            let second_min = previous
                .iter()
                .enumerate()
                .filter(|(index, _)| *index != min_index)
                .map(|(_, value)| *value)
                .min()
                .unwrap();
            let mut current = vec![0; color_count];
            for color in 0..color_count {
                let extra = if color == min_index { second_min } else { min_cost };
                current[color] = costs[row][color] + extra;
            }
            previous = current;
        }
        *previous.iter().min().unwrap()
    }
}
