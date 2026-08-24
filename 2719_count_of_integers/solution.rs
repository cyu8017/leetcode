// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

use std::collections::HashMap;

impl Solution {
    pub fn count(num1: String, num2: String, min_sum: i32, max_sum: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
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
        fn dp(s: &str, min_sum: i32, max_sum: i32) -> i32 {
            const MOD: i32 = 1_000_000_007;
            let bytes = s.as_bytes();
            let n = bytes.len();
            let mut memo: HashMap<(i32, i32, i32), i32> = HashMap::new();
            fn dfs(
                pos: usize,
                sum: i32,
                tight: bool,
                bytes: &[u8],
                n: usize,
                min_sum: i32,
                max_sum: i32,
                memo: &mut HashMap<(i32, i32, i32), i32>,
            ) -> i32 {
                if sum > max_sum {
                    return 0;
                }
                if pos == n {
                    return if sum >= min_sum { 1 } else { 0 };
                }
                let key = (pos as i32, sum, if tight { 1 } else { 0 });
                if let Some(&v) = memo.get(&key) {
                    return v;
                }
                let up = if tight { (bytes[pos] - b'0') as i32 } else { 9 };
                let mut res = 0;
                for d in 0..=up {
                    res = (res
                        + dfs(
                            pos + 1,
                            sum + d,
                            tight && d == up,
                            bytes,
                            n,
                            min_sum,
                            max_sum,
                            memo,
                        ))
                        % MOD;
                }
                memo.insert(key, res);
                res
            }
            dfs(0, 0, true, bytes, n, min_sum, max_sum, &mut memo)
        }
        let a = dp(&dec(num1), min_sum, max_sum);
        let b = dp(&num2, min_sum, max_sum);
        (b - a + MOD) % MOD
    }
}
