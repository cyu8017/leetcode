// LeetCode 2143 - Choose Numbers From Two Arrays in Range
// https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

use std::collections::HashMap;

impl Solution {
    pub fn count_subranges(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = nums1.len();
        let mut ans = 0;
        let mut dp: HashMap<i32, i32> = HashMap::new();
        for i in 0..n {
            let mut ndp: HashMap<i32, i32> = HashMap::new();
            *ndp.entry(nums1[i]).or_insert(0) = (ndp.get(&nums1[i]).unwrap_or(&0) + 1) % MOD;
            *ndp.entry(-nums2[i]).or_insert(0) = (ndp.get(&-nums2[i]).unwrap_or(&0) + 1) % MOD;
            for (&diff, &cnt) in &dp {
                *ndp.entry(diff + nums1[i]).or_insert(0) =
                    (ndp.get(&(diff + nums1[i])).unwrap_or(&0) + cnt) % MOD;
                *ndp.entry(diff - nums2[i]).or_insert(0) =
                    (ndp.get(&(diff - nums2[i])).unwrap_or(&0) + cnt) % MOD;
            }
            dp = ndp;
            ans = (ans + dp.get(&0).copied().unwrap_or(0)) % MOD;
        }
        ans
    }
}
