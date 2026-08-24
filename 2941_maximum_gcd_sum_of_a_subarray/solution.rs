// LeetCode 2941 - Maximum GCD-Sum of a Subarray
// https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

impl Solution {
    pub fn max_gcd_sum(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }
        let mut ans = 0i64;
        let mut st: Vec<(i32, usize)> = Vec::new();
        for i in 0..n {
            let mut nst = vec![(nums[i], i)];
            for &(g0, idx) in &st {
                let g = gcd(g0, nums[i]);
                if nst.last().unwrap().0 == g {
                    continue;
                }
                nst.push((g, idx));
            }
            st = nst;
            for &(g, idx) in &st {
                if (i - idx + 1) as i32 >= k {
                    let cand = (pref[i + 1] - pref[idx]) * g as i64;
                    if cand > ans {
                        ans = cand;
                    }
                }
            }
        }
        ans
    }
}
