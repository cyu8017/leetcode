// LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

use std::collections::HashMap;

impl Solution {
    pub fn max_happy_groups(batch_size: i32, groups: Vec<i32>) -> i32 {
        let batch_size = batch_size as usize;
        let mut count = vec![0i32; batch_size];
        for size in groups {
            count[(size as usize) % batch_size] += 1;
        }

        let mut memo: HashMap<(i32, Vec<i32>), i32> = HashMap::new();
        let mut ans = Self::dfs(0, count.clone(), batch_size, &mut memo);
        if count[0] > 0 {
            ans += count[0] - 1;
        }
        ans
    }

    fn dfs(
        remainder: i32,
        mut state: Vec<i32>,
        batch_size: usize,
        memo: &mut HashMap<(i32, Vec<i32>), i32>,
    ) -> i32 {
        let key = (remainder, state.clone());
        if let Some(&cached) = memo.get(&key) {
            return cached;
        }

        let mut best = 0;
        for mod_val in 1..batch_size {
            if state[mod_val] == 0 {
                continue;
            }
            state[mod_val] -= 1;
            best = best.max(Self::dfs(
                (remainder + mod_val as i32) % batch_size as i32,
                state.clone(),
                batch_size,
                memo,
            ));
            state[mod_val] += 1;
        }
        if remainder == 0 {
            best += 1;
        }
        memo.insert(key, best);
        best
    }
}
