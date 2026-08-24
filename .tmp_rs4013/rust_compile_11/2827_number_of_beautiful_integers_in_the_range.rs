struct Solution;
fn main() {}

// LeetCode 2827 - Number of Beautiful Integers in the Range
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_beautiful_integers(low: i32, high: i32, k: i32) -> i32 {
        fn count(n: i32, k: i32) -> i32 {
            if n < 0 {
                return 0;
            }
            let s = n.to_string();
            let b = s.as_bytes();
            let mut memo: HashMap<(i32, i32, i32, i32, i32), i32> = HashMap::new();
            fn dfs(
                pos: usize,
                diff: i32,
                modulo: i32,
                tight: i32,
                started: i32,
                b: &[u8],
                k: i32,
                memo: &mut HashMap<(i32, i32, i32, i32, i32), i32>,
            ) -> i32 {
                if pos == b.len() {
                    return if started == 1 && diff == 0 && modulo == 0 {
                        1
                    } else {
                        0
                    };
                }
                let key = (pos as i32, diff, modulo, tight, started);
                if let Some(&v) = memo.get(&key) {
                    return v;
                }
                let up = if tight == 1 { (b[pos] - b'0') as i32 } else { 9 };
                let mut ans = 0;
                for d in 0..=up {
                    let nt = if tight == 1 && d == up { 1 } else { 0 };
                    if started == 0 {
                        if d == 0 {
                            ans += dfs(pos + 1, diff, modulo, nt, 0, b, k, memo);
                        } else {
                            let nd = diff + if d % 2 == 0 { 1 } else { -1 };
                            ans += dfs(pos + 1, nd, d % k, nt, 1, b, k, memo);
                        }
                    } else {
                        let nd = diff + if d % 2 == 0 { 1 } else { -1 };
                        ans += dfs(pos + 1, nd, (modulo * 10 + d) % k, nt, 1, b, k, memo);
                    }
                }
                memo.insert(key, ans);
                ans
            }
            dfs(0, 0, 0, 1, 0, b, k, &mut memo)
        }
        count(high, k) - count(low - 1, k)
    }
}
