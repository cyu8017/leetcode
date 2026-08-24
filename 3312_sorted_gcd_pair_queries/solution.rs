// LeetCode 3312 - Sorted GCD Pair Queries
// https://leetcode.com/problems/sorted-gcd-pair-queries/

impl Solution {
    pub fn gcd_values(nums: Vec<i32>, queries: Vec<i64>) -> Vec<i32> {
        let max_v = *nums.iter().max().unwrap() as usize;
        let mut cnt = vec![0i64; max_v + 1];
        for x in nums {
            cnt[x as usize] += 1;
        }
        let mut div_cnt = vec![0i64; max_v + 1];
        for g in 1..=max_v {
            let mut c = 0i64;
            let mut m = g;
            while m <= max_v {
                c += cnt[m];
                m += g;
            }
            div_cnt[g] = c * (c - 1) / 2;
        }
        let mut exact = vec![0i64; max_v + 1];
        for g in (1..=max_v).rev() {
            exact[g] = div_cnt[g];
            let mut m = 2 * g;
            while m <= max_v {
                exact[g] -= exact[m];
                m += g;
            }
        }
        let mut pref = vec![0i64; max_v + 1];
        for g in 1..=max_v {
            pref[g] = pref[g - 1] + exact[g];
        }
        let mut ans = vec![0; queries.len()];
        for (i, &q) in queries.iter().enumerate() {
            let mut lo = 1;
            let mut hi = max_v as i32;
            while lo < hi {
                let mid = (lo + hi) / 2;
                if pref[mid as usize] > q {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            ans[i] = lo;
        }
        ans
    }
}
