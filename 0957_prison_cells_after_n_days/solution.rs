// LeetCode 0957 - Prison Cells After N Days
// https://leetcode.com/problems/prison-cells-after-n-days/

use std::collections::HashMap;

impl Solution {
    pub fn prison_after_n_days(cells: Vec<i32>, mut n: i32) -> Vec<i32> {
        let mut seen = HashMap::new();
        let mut state = cells;
        while n > 0 {
            if let Some(&prev) = seen.get(&state) {
                let cycle = prev - n;
                n %= cycle;
                if n == 0 {
                    break;
                }
            }
            seen.insert(state.clone(), n);
            let mut nxt = vec![0; 8];
            for i in 1..=6 {
                nxt[i] = if state[i - 1] == state[i + 1] { 1 } else { 0 };
            }
            state = nxt;
            n -= 1;
        }
        state
    }
}
