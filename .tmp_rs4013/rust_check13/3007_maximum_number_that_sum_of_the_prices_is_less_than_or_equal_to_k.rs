#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
// https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

impl Solution {
    pub fn find_maximum_number(k: i64, x: i32) -> i64 {
        let mut l = 1i64;
        let mut r = 10i64.pow(17);
        let mut num = 0i64;
        fn dfs(pos: i32, cnt: i32, limit: bool, num: i64, x: i32, f: &mut [[i64; 65]; 65]) -> i64 {
            if pos == 0 {
                return cnt as i64;
            }
            if !limit && f[pos as usize][cnt as usize] != -1 {
                return f[pos as usize][cnt as usize];
            }
            let mut ans = 0i64;
            let up = if limit {
                ((num >> (pos - 1)) & 1) as i32
            } else {
                1
            };
            for i in 0..=up {
                let mut v = cnt;
                if i == 1 && pos % x == 0 {
                    v += 1;
                }
                ans += dfs(pos - 1, v, limit && i == up, num, x, f);
            }
            if !limit {
                f[pos as usize][cnt as usize] = ans;
            }
            ans
        }
        while l < r {
            let mid = (l + r + 1) >> 1;
            num = mid;
            let m = if num == 0 {
                0
            } else {
                64 - num.leading_zeros() as i32
            };
            let mut f = [[-1i64; 65]; 65];
            if dfs(m, 0, true, num, x, &mut f) <= k {
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        l
    }
}
