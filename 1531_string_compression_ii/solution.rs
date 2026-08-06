// LeetCode 1531 - String Compression II
// https://leetcode.com/problems/string-compression-ii/

use std::collections::HashMap;

impl Solution {
    pub fn get_length_of_optimal_compression(s: String, k: i32) -> i32 {
        let n = s.len();
        let s = s.into_bytes();
        const INF: i32 = 1_000_000_000;
        let mut memo: HashMap<(usize, i32), i32> = HashMap::new();

        fn dp(
            index: usize,
            remaining: i32,
            s: &[u8],
            n: usize,
            memo: &mut HashMap<(usize, i32), i32>,
        ) -> i32 {
            if remaining < 0 {
                return INF;
            }
            if index == n || n - index <= remaining as usize {
                return 0;
            }
            if let Some(&v) = memo.get(&(index, remaining)) {
                return v;
            }
            let mut answer = dp(index + 1, remaining - 1, s, n, memo);
            let mut same = 0;
            let mut removed = 0;
            for j in index..n {
                if s[j] == s[index] {
                    same += 1;
                    let mut encoded = 1;
                    if same >= 2 {
                        encoded += 1;
                    }
                    if same >= 10 {
                        encoded += 1;
                    }
                    if same >= 100 {
                        encoded += 1;
                    }
                    answer = answer.min(encoded + dp(j + 1, remaining - removed, s, n, memo));
                } else {
                    removed += 1;
                    if removed > remaining {
                        break;
                    }
                }
            }
            memo.insert((index, remaining), answer);
            answer
        }

        dp(0, k, &s, n, &mut memo)
    }
}
