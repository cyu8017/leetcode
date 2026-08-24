// LeetCode 0691 - Stickers to Spell Word
// https://leetcode.com/problems/stickers-to-spell-word/

use std::collections::HashMap;

impl Solution {
    pub fn min_stickers(stickers: Vec<String>, target: String) -> i32 {
        let mut need = [0i32; 26];
        for ch in target.bytes() {
            need[(ch - b'a') as usize] += 1;
        }
        let chars: Vec<u8> = (0..26)
            .filter(|&i| need[i] > 0)
            .map(|i| b'a' + i as u8)
            .collect();
        let mut sticks = Vec::new();
        for sticker in stickers {
            let mut counts = [0i32; 26];
            for ch in sticker.bytes() {
                counts[(ch - b'a') as usize] += 1;
            }
            if chars.iter().any(|&ch| counts[(ch - b'a') as usize] > 0) {
                sticks.push(counts);
            }
        }
        let state: Vec<i32> = chars.iter().map(|&ch| need[(ch - b'a') as usize]).collect();
        let mut memo = HashMap::new();
        let result = Self::dfs(&state, &chars, &sticks, &mut memo);
        if result >= i32::MAX / 4 {
            -1
        } else {
            result
        }
    }

    fn dfs(
        state: &[i32],
        chars: &[u8],
        sticks: &[[i32; 26]],
        memo: &mut HashMap<Vec<i32>, i32>,
    ) -> i32 {
        if let Some(&cached) = memo.get(state) {
            return cached;
        }
        if state.iter().all(|&c| c == 0) {
            memo.insert(state.to_vec(), 0);
            return 0;
        }
        let first = chars[state.iter().position(|&c| c > 0).unwrap()];
        let mut best = i32::MAX / 4;
        for stick in sticks {
            if stick[(first - b'a') as usize] == 0 {
                continue;
            }
            let nxt: Vec<i32> = state
                .iter()
                .enumerate()
                .map(|(j, &cnt)| (cnt - stick[(chars[j] - b'a') as usize]).max(0))
                .collect();
            best = best.min(1 + Self::dfs(&nxt, chars, sticks, memo));
        }
        memo.insert(state.to_vec(), best);
        best
    }
}
