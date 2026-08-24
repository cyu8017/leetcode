struct Solution;
fn main() {}

// LeetCode 2801 - Count Stepping Numbers in Range
// https://leetcode.com/problems/count-stepping-numbers-in-range/

use std::collections::HashMap;

impl Solution {
    pub fn count_stepping_numbers(low: String, high: String) -> i32 {
        const MOD: i32 = 1_000_000_007;
        fn count_to(s: &str) -> i32 {
            let b = s.as_bytes();
            let mut memo: HashMap<(i32, i32, i32, i32), i32> = HashMap::new();
            fn dfs(
                pos: usize,
                tight: i32,
                last: i32,
                started: i32,
                b: &[u8],
                memo: &mut HashMap<(i32, i32, i32, i32), i32>,
            ) -> i32 {
                if pos == b.len() {
                    return started;
                }
                let key = (pos as i32, tight, last, started);
                if let Some(&v) = memo.get(&key) {
                    return v;
                }
                let up = if tight == 1 { (b[pos] - b'0') as i32 } else { 9 };
                let mut ans = 0i64;
                for d in 0..=up {
                    let nt = if tight == 1 && d == up { 1 } else { 0 };
                    if started == 0 {
                        if d == 0 {
                            ans += dfs(pos + 1, nt, -1, 0, b, memo) as i64;
                        } else {
                            ans += dfs(pos + 1, nt, d, 1, b, memo) as i64;
                        }
                    } else if (d - last).abs() == 1 {
                        ans += dfs(pos + 1, nt, d, 1, b, memo) as i64;
                    }
                }
                let res = (ans % 1_000_000_007) as i32;
                memo.insert(key, res);
                res
            }
            dfs(0, 1, -1, 0, b, &mut memo)
        }
        fn dec(mut s: String) -> String {
            let mut b = s.into_bytes();
            let mut i = b.len() as i32 - 1;
            while i >= 0 && b[i as usize] == b'0' {
                b[i as usize] = b'9';
                i -= 1;
            }
            if i >= 0 {
                b[i as usize] -= 1;
            }
            let mut j = 0;
            while j + 1 < b.len() && b[j] == b'0' {
                j += 1;
            }
            String::from_utf8(b[j..].to_vec()).unwrap()
        }
        let mut ans = (count_to(&high) - count_to(&dec(low))) % MOD;
        if ans < 0 {
            ans += MOD;
        }
        ans
    }
}
