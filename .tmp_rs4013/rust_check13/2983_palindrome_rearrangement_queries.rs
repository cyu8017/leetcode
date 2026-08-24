#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2983 - Palindrome Rearrangement Queries
// https://leetcode.com/problems/palindrome-rearrangement-queries/

impl Solution {
    pub fn can_make_palindrome_queries(s: String, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n = s.len();
        let m = n / 2;
        let bytes = s.as_bytes();
        let mut t: Vec<u8> = bytes[m..].to_vec();
        t.reverse();
        let s = bytes[..m].to_vec();

        let mut pre1 = vec![vec![0i32; 26]; m + 1];
        let mut pre2 = vec![vec![0i32; 26]; m + 1];
        let mut diff = vec![0i32; m + 1];
        for i in 1..=m {
            pre1[i] = pre1[i - 1].clone();
            pre2[i] = pre2[i - 1].clone();
            pre1[i][(s[i - 1] - b'a') as usize] += 1;
            pre2[i][(t[i - 1] - b'a') as usize] += 1;
            diff[i] = diff[i - 1] + if s[i - 1] == t[i - 1] { 0 } else { 1 };
        }

        fn count(pre: &[Vec<i32>], i: usize, j: usize) -> Vec<i32> {
            let mut cnt = vec![0; 26];
            for k in 0..26 {
                cnt[k] = pre[j + 1][k] - pre[i][k];
            }
            cnt
        }
        fn sub(cnt1: &[i32], cnt2: &[i32]) -> Option<Vec<i32>> {
            let mut cnt = vec![0; 26];
            for i in 0..26 {
                cnt[i] = cnt1[i] - cnt2[i];
                if cnt[i] < 0 {
                    return None;
                }
            }
            Some(cnt)
        }
        fn check(
            pre1: &[Vec<i32>],
            pre2: &[Vec<i32>],
            diff: &[i32],
            a: usize,
            b: usize,
            c: usize,
            d: usize,
        ) -> bool {
            if diff[a] > 0 || diff[diff.len() - 1] - diff[(b.max(d) + 1).min(diff.len() - 1)] > 0 {
                return false;
            }
            if d <= b {
                return count(pre1, a, b) == count(pre2, a, b);
            }
            if b < c {
                return diff[c] - diff[b + 1] == 0
                    && count(pre1, a, b) == count(pre2, a, b)
                    && count(pre1, c, d) == count(pre2, c, d);
            }
            match (sub(&count(pre1, a, b), &count(pre2, a, c - 1)), sub(&count(pre2, c, d), &count(pre1, b + 1, d))) {
                (Some(c1), Some(c2)) => c1 == c2,
                _ => false,
            }
        }

        let mut ans = vec![false; queries.len()];
        for (i, q) in queries.iter().enumerate() {
            let a = q[0] as usize;
            let b = q[1] as usize;
            let c = n - 1 - q[3] as usize;
            let d = n - 1 - q[2] as usize;
            ans[i] = if a <= c {
                check(&pre1, &pre2, &diff, a, b, c, d)
            } else {
                check(&pre2, &pre1, &diff, c, d, a, b)
            };
        }
        ans
    }
}
