// LeetCode 1044 - Longest Duplicate Substring
// https://leetcode.com/problems/longest-duplicate-substring/

use std::collections::HashMap;

impl Solution {
    pub fn longest_dup_substring(s: String) -> String {
        const MOD: u128 = (1u128 << 61) - 1;
        const BASE: u128 = 256;
        let n = s.len();
        let nums: Vec<u128> = s.bytes().map(|b| b as u128).collect();
        let bytes = s.as_bytes();

        let search = |length: usize| -> isize {
            if length == 0 {
                return 0;
            }
            let mut h: u128 = 0;
            for i in 0..length {
                h = (h * BASE + nums[i]) % MOD;
            }
            let mut seen: HashMap<u128, Vec<usize>> = HashMap::new();
            seen.insert(h, vec![0]);
            let mut power: u128 = 1;
            for _ in 0..length {
                power = (power * BASE) % MOD;
            }
            for i in 1..=n - length {
                h = (h * BASE + MOD - (nums[i - 1] * power) % MOD + nums[i + length - 1]) % MOD;
                if let Some(positions) = seen.get(&h) {
                    let cur = &bytes[i..i + length];
                    for &j in positions {
                        if &bytes[j..j + length] == cur {
                            return i as isize;
                        }
                    }
                    seen.get_mut(&h).unwrap().push(i);
                } else {
                    seen.insert(h, vec![i]);
                }
            }
            -1
        };

        let mut lo = 0usize;
        let mut hi = n - 1;
        let mut start: isize = -1;
        let mut best_len = 0usize;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            let pos = search(mid);
            if pos >= 0 {
                start = pos;
                best_len = mid;
                lo = mid + 1;
            } else if mid == 0 {
                break;
            } else {
                hi = mid - 1;
            }
        }
        if start >= 0 {
            s[start as usize..start as usize + best_len].to_string()
        } else {
            String::new()
        }
    }
}
