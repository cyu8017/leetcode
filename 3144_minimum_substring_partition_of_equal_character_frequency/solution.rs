// LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
// https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_substrings_in_partition(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut memo = vec![-1i32; n];
        fn dfs(b: &[u8], i: usize, memo: &mut [i32]) -> i32 {
            let n = b.len();
            if i >= n {
                return 0;
            }
            if memo[i] != -1 {
                return memo[i];
            }
            let mut cnt = [0i32; 26];
            let mut freq: HashMap<i32, i32> = HashMap::new();
            memo[i] = (n - i) as i32;
            for j in i..n {
                let k = (b[j] - b'a') as usize;
                if cnt[k] > 0 {
                    let e = freq.get_mut(&cnt[k]).unwrap();
                    *e -= 1;
                    if *e == 0 {
                        freq.remove(&cnt[k]);
                    }
                }
                cnt[k] += 1;
                *freq.entry(cnt[k]).or_insert(0) += 1;
                if freq.len() == 1 {
                    memo[i] = memo[i].min(1 + dfs(b, j + 1, memo));
                }
            }
            memo[i]
        }
        dfs(b, 0, &mut memo)
    }
}
