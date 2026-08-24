// LeetCode 3261 - Count Substrings That Satisfy K-Constraint II
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

impl Solution {
    pub fn count_k_constraint_substrings(s: String, k: i32, queries: Vec<Vec<i32>>) -> Vec<i64> {
        let b = s.as_bytes();
        let n = b.len();
        let mut left_most = vec![0; n];
        let mut z = 0;
        let mut o = 0;
        let mut l = 0;
        for r in 0..n {
            if b[r] == b'0' {
                z += 1;
            } else {
                o += 1;
            }
            while z > k && o > k {
                if b[l] == b'0' {
                    z -= 1;
                } else {
                    o -= 1;
                }
                l += 1;
            }
            left_most[r] = l;
        }
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + (i - left_most[i] + 1) as i64;
        }
        let mut ans = vec![0i64; queries.len()];
        for (qi, q) in queries.iter().enumerate() {
            let lq = q[0] as usize;
            let rq = q[1] as usize;
            let mut lo = lq;
            let mut hi = rq + 1;
            while lo < hi {
                let mid = (lo + hi) / 2;
                if left_most[mid] < lq {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            let mut res = 0i64;
            if lo > lq {
                let m = (lo - lq) as i64;
                res += m * (m + 1) / 2;
            }
            if lo <= rq {
                res += pref[rq + 1] - pref[lo];
            }
            ans[qi] = res;
        }
        ans
    }
}
