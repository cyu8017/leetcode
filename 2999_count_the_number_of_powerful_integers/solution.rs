// LeetCode 2999 - Count the Number of Powerful Integers
// https://leetcode.com/problems/count-the-number-of-powerful-integers/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_powerful_int(start: i64, finish: i64, limit: i32, s: String) -> i64 {
        fn count(num: i64, limit: i32, s: &str) -> i64 {
            if num < 0 {
                return 0;
            }
            for c in s.bytes() {
                if (c - b'0') as i32 > limit {
                    return 0;
                }
            }
            let t = num.to_string();
            let n = t.len();
            let sn = s.len();
            if n < sn {
                return 0;
            }
            let mut ans = 0i64;
            for length in sn..n {
                let pre_len = length - sn;
                if pre_len == 0 {
                    ans += 1;
                } else {
                    let mut ways = limit as i64;
                    for _ in 1..pre_len {
                        ways *= (limit + 1) as i64;
                    }
                    ans += ways;
                }
            }
            let pref = n - sn;
            let tb = t.as_bytes();
            fn dfs(
                i: usize,
                tight: bool,
                pref: usize,
                tb: &[u8],
                s: &str,
                limit: i32,
                memo: &mut HashMap<(usize, i32), i64>,
            ) -> i64 {
                if i == pref {
                    if tight {
                        return if &tb[pref..] >= s.as_bytes() { 1 } else { 0 };
                    }
                    return 1;
                }
                let key = (i, if tight { 1 } else { 0 });
                if let Some(&v) = memo.get(&key) {
                    return v;
                }
                let mut up = if tight { (tb[i] - b'0') as i32 } else { limit };
                if up > limit {
                    up = limit;
                }
                let mut res = 0i64;
                for d in 0..=up {
                    if i == 0 && d == 0 {
                        continue;
                    }
                    res += dfs(i + 1, tight && d == (tb[i] - b'0') as i32, pref, tb, s, limit, memo);
                }
                memo.insert(key, res);
                res
            }
            let mut memo = HashMap::new();
            ans += dfs(0, true, pref, tb, s, limit, &mut memo);
            ans
        }
        count(finish, limit, &s) - count(start - 1, limit, &s)
    }
}
