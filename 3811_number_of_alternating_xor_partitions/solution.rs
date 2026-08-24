// LeetCode 3811 - Number Of Alternating Xor Partitions
// https://leetcode.com/problems/number-of-alternating-xor-partitions/

use std::collections::HashMap;

impl Solution {
    pub fn alternating_xor(nums: Vec<i32>, target1: i32, target2: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut cnt1: HashMap<i32, i32> = HashMap::new();
        let mut cnt2: HashMap<i32, i32> = HashMap::new();
        cnt2.insert(0, 1);
        let mut pre = 0;
        let mut ans = 0;
        for x in nums {
            pre ^= x;
            let a = *cnt2.get(&(pre ^ target1)).unwrap_or(&0);
            let b = *cnt1.get(&(pre ^ target2)).unwrap_or(&0);
            ans = (a + b) % MOD;
            *cnt1.entry(pre).or_insert(0) = (cnt1.get(&pre).copied().unwrap_or(0) + a) % MOD;
            *cnt2.entry(pre).or_insert(0) = (cnt2.get(&pre).copied().unwrap_or(0) + b) % MOD;
        }
        ans
    }
}
