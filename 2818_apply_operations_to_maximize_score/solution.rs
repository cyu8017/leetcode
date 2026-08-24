// LeetCode 2818 - Apply Operations to Maximize Score
// https://leetcode.com/problems/apply-operations-to-maximize-score/

use std::collections::HashSet;

impl Solution {
    pub fn maximum_score(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let max_v = *nums.iter().max().unwrap();
        let mut spf = vec![0i32; (max_v + 1) as usize];
        for i in 2..=max_v {
            if spf[i as usize] == 0 {
                let mut j = i;
                while j <= max_v {
                    if spf[j as usize] == 0 {
                        spf[j as usize] = i;
                    }
                    j += i;
                }
            }
        }
        let prime_score = |mut x: i32| {
            let mut seen = HashSet::new();
            while x > 1 {
                let p = spf[x as usize];
                seen.insert(p);
                while x % p == 0 {
                    x /= p;
                }
            }
            seen.len() as i32
        };
        let score: Vec<i32> = nums.iter().map(|&v| prime_score(v)).collect();
        let mut left = vec![0i32; n];
        let mut right = vec![0i32; n];
        let mut st = Vec::new();
        for i in 0..n {
            while !st.is_empty() && score[*st.last().unwrap()] < score[i] {
                st.pop();
            }
            left[i] = if st.is_empty() { -1 } else { *st.last().unwrap() as i32 };
            st.push(i);
        }
        st.clear();
        for i in (0..n).rev() {
            while !st.is_empty() && score[*st.last().unwrap()] <= score[i] {
                st.pop();
            }
            right[i] = if st.is_empty() { n as i32 } else { *st.last().unwrap() as i32 };
            st.push(i);
        }
        let mut arr: Vec<(i32, i64)> = (0..n)
            .map(|i| (nums[i], (i as i64 - left[i] as i64) * (right[i] as i64 - i as i64)))
            .collect();
        arr.sort_unstable_by(|a, b| b.0.cmp(&a.0));
        fn mod_pow(mut a: i64, mut b: i64) -> i64 {
            let mut res = 1i64;
            a %= MOD;
            while b > 0 {
                if b & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                b >>= 1;
            }
            res
        }
        let mut ans = 1i64;
        let mut remain = k as i64;
        for (v, cnt) in arr {
            if remain <= 0 {
                break;
            }
            let use_cnt = cnt.min(remain);
            ans = ans * mod_pow(v as i64, use_cnt) % MOD;
            remain -= use_cnt;
        }
        ans as i32
    }
}
