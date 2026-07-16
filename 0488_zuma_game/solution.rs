// LeetCode 0488 - Zuma Game
// https://leetcode.com/problems/zuma-game/

use std::collections::HashMap;

impl Solution {
    fn shrink(s: String) -> String {
        let bytes = s.into_bytes();
        let mut index = 0usize;
        while index < bytes.len() {
            let mut end = index;
            while end < bytes.len() && bytes[end] == bytes[index] {
                end += 1;
            }
            if end - index >= 3 {
                let mut next = bytes[..index].to_vec();
                next.extend_from_slice(&bytes[end..]);
                return Self::shrink(String::from_utf8(next).unwrap());
            }
            index = end;
        }
        String::from_utf8(bytes).unwrap()
    }

    fn dfs(board: String, hand: String, memo: &mut HashMap<String, i32>) -> i32 {
        let key = format!("{board}#{hand}");
        if let Some(value) = memo.get(&key) {
            return *value;
        }
        let board = Self::shrink(board);
        if board.is_empty() {
            memo.insert(key, 0);
            return 0;
        }
        let mut best = i32::MAX;
        let board_bytes = board.as_bytes();
        let hand_bytes = hand.as_bytes();
        for insert in 0..=board_bytes.len() {
            for pick in 0..hand_bytes.len() {
                let color = hand_bytes[pick];
                let allowed = (insert < board_bytes.len() && board_bytes[insert] == color)
                    || (insert > 0 && board_bytes[insert - 1] == color);
                if !allowed {
                    continue;
                }
                let mut next_board = String::new();
                next_board.push_str(&board[..insert]);
                next_board.push(color as char);
                next_board.push_str(&board[insert..]);
                let next_board = Self::shrink(next_board);
                if next_board == board {
                    continue;
                }
                let next_hand = format!("{}{}", &hand[..pick], &hand[pick + 1..]);
                let steps = Self::dfs(next_board, next_hand, memo);
                if steps != i32::MAX {
                    best = best.min(steps + 1);
                }
            }
        }
        memo.insert(key, best);
        best
    }

    pub fn find_min_step(board: String, hand: String) -> i32 {
        let mut memo = HashMap::new();
        let result = Self::dfs(board, hand, &mut memo);
        if result == i32::MAX {
            -1
        } else {
            result
        }
    }
}
