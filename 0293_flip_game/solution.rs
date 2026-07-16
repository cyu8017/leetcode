// LeetCode 0293 - Flip Game
// https://leetcode.com/problems/flip-game/

impl Solution {
    pub fn generate_possible_next_moves(current_state: String) -> Vec<String> {
        let mut state = current_state.into_bytes();
        let mut result = Vec::new();

        for index in 0..state.len().saturating_sub(1) {
            if state[index] == b'+' && state[index + 1] == b'+' {
                let mut next_state = state.clone();
                next_state[index] = b'-';
                next_state[index + 1] = b'-';
                result.push(String::from_utf8(next_state).unwrap());
            }
        }

        result
    }
}
