// LeetCode 1686 - Stone Game VI
// https://leetcode.com/problems/stone-game-vi/

impl Solution {
    pub fn stone_game_vi(alice_values: Vec<i32>, bob_values: Vec<i32>) -> i32 {
        let mut order: Vec<usize> = (0..alice_values.len()).collect();
        order.sort_by_key(|&i| std::cmp::Reverse(alice_values[i] + bob_values[i]));
        let mut score = 0i32;
        for (t, &i) in order.iter().enumerate() {
            if t % 2 == 0 {
                score += alice_values[i];
            } else {
                score -= bob_values[i];
            }
        }
        score.signum()
    }
}
