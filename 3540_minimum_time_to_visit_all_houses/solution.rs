// LeetCode 3540 - Minimum Time to Visit All Houses
// https://leetcode.com/problems/minimum-time-to-visit-all-houses/

impl Solution {
    pub fn min_total_time(forward: Vec<i32>, backward: Vec<i32>, queries: Vec<i32>) -> i64 {
        let n = forward.len();
        let sum_b: i32 = backward.iter().sum();
        let mut pf = vec![0i32; n + 1];
        let mut pb = vec![0i32; n + 1];
        for i in 0..n {
            pf[i + 1] = pf[i] + forward[i];
            pb[i + 1] = pb[i] + backward[i];
        }
        let mut ans = 0i64;
        let mut pos = 0i32;
        for q in queries {
            let mut r = 0;
            if q < pos {
                r = pf[n];
            }
            r += pf[q as usize] - pf[pos as usize];
            let mut lft = 0;
            if q > pos {
                lft = sum_b;
            }
            lft += pb[pos as usize] - pb[q as usize];
            ans += lft.min(r) as i64;
            pos = q;
        }
        ans
    }
}
