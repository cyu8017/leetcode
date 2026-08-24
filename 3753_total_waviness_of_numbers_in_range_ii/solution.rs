// LeetCode 3753 - Total Waviness of Numbers in Range II
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

use std::collections::HashMap;

#[derive(Clone, Copy, Default)]
struct Result {
    count: i64,
    sum: i64,
}

impl Solution {
    fn waviness_up_to(limit: i64) -> i64 {
        if limit < 0 {
            return 0;
        }
        let mut digits = Vec::new();
        if limit == 0 {
            digits.push(0);
        } else {
            let mut value = limit;
            while value > 0 {
                digits.push((value % 10) as i32);
                value /= 10;
            }
            digits.reverse();
        }
        let mut memo: HashMap<(i32, i32, i32, bool), Result> = HashMap::new();

        fn dfs(
            position: usize,
            second_last: i32,
            last: i32,
            started: bool,
            tight: bool,
            digits: &[i32],
            memo: &mut HashMap<(i32, i32, i32, bool), Result>,
        ) -> Result {
            if position == digits.len() {
                return Result { count: 1, sum: 0 };
            }
            let key = (position as i32, second_last, last, started);
            if !tight {
                if let Some(&cached) = memo.get(&key) {
                    return cached;
                }
            }
            let upper = if tight { digits[position] } else { 9 };
            let mut result = Result::default();
            for digit in 0..=upper {
                let next_tight = tight && digit == upper;
                let mut next_second_last = second_last;
                let mut next_last = last;
                let next_started = started || digit != 0;
                let mut add = 0i64;
                if !next_started {
                    next_second_last = 10;
                    next_last = 10;
                } else if !started {
                    next_second_last = 10;
                    next_last = digit;
                } else {
                    if second_last != 10
                        && ((last > second_last && last > digit)
                            || (last < second_last && last < digit))
                    {
                        add = 1;
                    }
                    next_second_last = last;
                    next_last = digit;
                }
                let child = dfs(
                    position + 1,
                    next_second_last,
                    next_last,
                    next_started,
                    next_tight,
                    digits,
                    memo,
                );
                result.count += child.count;
                result.sum += child.sum + add * child.count;
            }
            if !tight {
                memo.insert(key, result);
            }
            result
        }

        dfs(0, 10, 10, false, true, &digits, &mut memo).sum
    }

    pub fn total_waviness(a: i64, b: i64) -> i64 {
        Self::waviness_up_to(b) - Self::waviness_up_to(a - 1)
    }
}
