#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2967 - Minimum Cost to Make Array Equalindromic
// https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

impl Solution {
    pub fn minimum_cost(mut nums: Vec<i32>) -> i64 {
        nums.sort_unstable();
        let n = nums.len();
        let median = nums[n / 2];
        fn make_pal(x: i32) -> i32 {
            let mut s: Vec<u8> = x.to_string().into_bytes();
            let mut i = 0;
            let mut j = s.len() - 1;
            while i < j {
                s[j] = s[i];
                i += 1;
                j -= 1;
            }
            String::from_utf8(s).unwrap().parse().unwrap_or(0)
        }
        let mut candidates = Vec::new();
        candidates.push(make_pal(median));
        let s = median.to_string();
        let half: i32 = s[..(s.len() + 1) / 2].parse().unwrap();
        for d in -2..=2 {
            let h = half + d;
            if h <= 0 {
                continue;
            }
            let hs = h.to_string();
            let pal = if s.len() % 2 == 0 {
                let mut rb = hs.clone();
                let rev: String = rb.chars().rev().collect();
                hs + &rev
            } else {
                let prefix: String = hs.chars().take(hs.len() - 1).collect();
                let rev: String = prefix.chars().rev().collect();
                hs + &rev
            };
            if let Ok(v) = pal.parse::<i32>() {
                candidates.push(v);
            }
        }
        for v in [1, 9, 11, 99, 101] {
            candidates.push(v);
        }
        let cost = |p: i32| -> i64 {
            nums.iter().map(|&v| (v as i64 - p as i64).abs()).sum()
        };
        let mut ans = 1i64 << 62;
        for p in candidates {
            if p <= 0 {
                continue;
            }
            ans = ans.min(cost(p));
        }
        ans
    }
}
