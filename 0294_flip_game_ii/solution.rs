// LeetCode 0294 - Flip Game II
// https://leetcode.com/problems/flip-game-ii/

use std::collections::HashMap;

impl Solution {
    pub fn can_win(current_state: String) -> bool {
        let mut memo: HashMap<String, bool> = HashMap::new();

        fn can_win_state(state: &str, memo: &mut HashMap<String, bool>) -> bool {
            if let Some(&value) = memo.get(state) {
                return value;
            }

            let mut bytes = state.as_bytes().to_vec();
            for index in 0..bytes.len().saturating_sub(1) {
                if bytes[index] == b'+' && bytes[index + 1] == b'+' {
                    bytes[index] = b'-';
                    bytes[index + 1] = b'-';
                    let next_state = String::from_utf8(bytes.clone()).unwrap();
                    bytes[index] = b'+';
                    bytes[index + 1] = b'+';
                    if !can_win_state(&next_state, memo) {
                        memo.insert(state.to_string(), true);
                        return true;
                    }
                }
            }

            memo.insert(state.to_string(), false);
            false
        }

        can_win_state(&current_state, &mut memo)
    }
}
