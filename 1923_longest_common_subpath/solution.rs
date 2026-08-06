// LeetCode 1923 - Longest Common Subpath
// https://leetcode.com/problems/longest-common-subpath/

use std::collections::HashSet;

impl Solution {
    pub fn longest_common_subpath(n: i32, paths: Vec<Vec<i32>>) -> i32 {
        let _ = n;
        const BASE1: i64 = 911_382_323;
        const MOD1: i64 = 1_000_000_007;
        const BASE2: i64 = 972_663_749;
        const MOD2: i64 = 1_000_000_009;

        fn mod_pow(mut base: i64, mut exp: i64, modulus: i64) -> i64 {
            let mut result = 1i64;
            base %= modulus;
            while exp > 0 {
                if exp & 1 == 1 {
                    result = result * base % modulus;
                }
                base = base * base % modulus;
                exp >>= 1;
            }
            result
        }

        fn has_common(paths: &[Vec<i32>], length: usize) -> bool {
            if length == 0 {
                return true;
            }
            let mut common: Option<HashSet<(i64, i64)>> = None;
            let pow1 = mod_pow(BASE1, length as i64, MOD1);
            let pow2 = mod_pow(BASE2, length as i64, MOD2);
            for path in paths {
                if path.len() < length {
                    return false;
                }
                let mut h1 = 0i64;
                let mut h2 = 0i64;
                let mut seen = HashSet::new();
                for (i, &city) in path.iter().enumerate() {
                    h1 = (h1 * BASE1 + city as i64 + 1) % MOD1;
                    h2 = (h2 * BASE2 + city as i64 + 1) % MOD2;
                    if i >= length {
                        h1 = (h1 - (path[i - length] as i64 + 1) * pow1 % MOD1 + MOD1) % MOD1;
                        h2 = (h2 - (path[i - length] as i64 + 1) * pow2 % MOD2 + MOD2) % MOD2;
                    }
                    if i + 1 >= length {
                        seen.insert((h1, h2));
                    }
                }
                match common {
                    None => common = Some(seen),
                    Some(ref mut set) => {
                        set.retain(|h| seen.contains(h));
                        if set.is_empty() {
                            return false;
                        }
                    }
                }
            }
            true
        }

        let mut lo = 0;
        let mut hi = paths.iter().map(|p| p.len()).min().unwrap_or(0);
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if has_common(&paths, mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo as i32
    }
}
