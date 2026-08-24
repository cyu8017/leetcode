// LeetCode 2067 - Number of Equal Count Substrings
// https://leetcode.com/problems/number-of-equal-count-substrings/

use std::collections::HashSet;

impl Solution {
    pub fn equal_count_substrings(s: String, count: i32) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let unique: HashSet<u8> = b.iter().copied().collect();
        let max_unique = unique.len();
        let mut ans = 0;
        for u in 1..=max_unique {
            let need_len = u * count as usize;
            if need_len > n {
                break;
            }
            let mut freq = [0i32; 26];
            let mut have = 0;
            for i in 0..n {
                let c = (b[i] - b'a') as usize;
                freq[c] += 1;
                if freq[c] == count {
                    have += 1;
                } else if freq[c] == count + 1 {
                    have -= 1;
                }
                if i >= need_len {
                    let p = (b[i - need_len] - b'a') as usize;
                    if freq[p] == count {
                        have -= 1;
                    } else if freq[p] == count + 1 {
                        have += 1;
                    }
                    freq[p] -= 1;
                }
                if i + 1 >= need_len && have == u {
                    ans += 1;
                }
            }
        }
        ans
    }
}
