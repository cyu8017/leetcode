// LeetCode 3966 - Count Good Integers in a Range
// https://leetcode.com/problems/count-good-integers-in-a-range/

use std::collections::HashMap;

impl Solution {
    pub fn count_good_integers(l: i64, r: i64, k: i32) -> i64 {
        fn count(bound: i64, k: i32) -> i64 {
            if bound <= 0 {
                return 0;
            }
            let digits: Vec<u8> = bound.to_string().bytes().collect();
            let mut memo: HashMap<(i32, i32, bool), i64> = HashMap::new();
            fn dfs(
                position: usize,
                previous: i32,
                started: bool,
                tight: bool,
                digits: &[u8],
                k: i32,
                memo: &mut HashMap<(i32, i32, bool), i64>,
            ) -> i64 {
                if position == digits.len() {
                    return if started { 1 } else { 0 };
                }
                let key = (position as i32, previous, started);
                if !tight {
                    if let Some(&v) = memo.get(&key) {
                        return v;
                    }
                }
                let limit = if tight { (digits[position] - b'0') as i32 } else { 9 };
                let mut result = 0i64;
                for digit in 0..=limit {
                    let next_started = started || digit != 0;
                    if started && (previous - digit).abs() > k {
                        continue;
                    }
                    let next_previous = if next_started { digit } else { previous };
                    result += dfs(
                        position + 1,
                        next_previous,
                        next_started,
                        tight && digit == limit,
                        digits,
                        k,
                        memo,
                    );
                }
                if !tight {
                    memo.insert(key, result);
                }
                result
            }
            dfs(0, 0, false, true, &digits, k, &mut memo)
        }
        count(r, k) - count(l - 1, k)
    }
}
