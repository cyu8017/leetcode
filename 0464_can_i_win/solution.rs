// LeetCode 0464 - Can I Win
// https://leetcode.com/problems/can-i-win/

use std::collections::HashMap;

impl Solution {
    fn can_win_state(
        state: i32,
        current_total: i32,
        max_choosable_integer: i32,
        desired_total: i32,
        memo: &mut HashMap<i32, bool>,
    ) -> bool {
        if let Some(&result) = memo.get(&state) {
            return result;
        }
        for pick in 1..=max_choosable_integer {
            let bit = 1 << (pick - 1);
            if state & bit != 0 {
                continue;
            }
            if current_total + pick >= desired_total {
                memo.insert(state, true);
                return true;
            }
            if !Self::can_win_state(
                state | bit,
                current_total + pick,
                max_choosable_integer,
                desired_total,
                memo,
            ) {
                memo.insert(state, true);
                return true;
            }
        }
        memo.insert(state, false);
        false
    }

    pub fn can_i_win(max_choosable_integer: i32, desired_total: i32) -> bool {
        if desired_total <= 0 {
            return true;
        }
        let total = max_choosable_integer * (max_choosable_integer + 1) / 2;
        if total < desired_total {
            return false;
        }
        let mut memo = HashMap::new();
        Self::can_win_state(0, 0, max_choosable_integer, desired_total, &mut memo)
    }
}
