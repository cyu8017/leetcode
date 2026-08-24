struct Solution;
// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

use std::collections::HashMap;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32, m: i32) -> i64 {
        let f = |lim: i32| {
            let mut cnt = HashMap::new();
            let mut ans = 0i64;
            let mut l = 0usize;
            let mut t = 0;
            for &x in &nums {
                let e = cnt.entry(x).or_insert(0);
                *e += 1;
                if *e == m {
                    t += 1;
                }
                while cnt.len() as i32 >= lim && t >= k {
                    let y = nums[l];
                    l += 1;
                    let e = cnt.get_mut(&y).unwrap();
                    *e -= 1;
                    if *e == m - 1 {
                        t -= 1;
                    }
                    if *e == 0 {
                        cnt.remove(&y);
                    }
                }
                ans += l as i64;
            }
            ans
        };
        f(k) - f(k + 1)
    }
}
