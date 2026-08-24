// LeetCode 3630 - Partition Array for Maximum XOR and AND
// https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/

impl Solution {
    pub fn maximize_xor_and_xor(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut best = 0i64;
        for mask in 0..(1 << n) {
            let mut and_val = -1;
            let mut xor_rest = 0;
            for i in 0..n {
                if (mask >> i) & 1 == 1 {
                    and_val = if and_val < 0 { nums[i] } else { and_val & nums[i] };
                } else {
                    xor_rest ^= nums[i];
                }
            }
            if and_val < 0 {
                and_val = 0;
            }
            let comp = ((1 << n) - 1) ^ mask;
            let mut sub = comp;
            loop {
                let mut x1 = 0;
                for i in 0..n {
                    if (sub >> i) & 1 == 1 {
                        x1 ^= nums[i];
                    }
                }
                let x2 = xor_rest ^ x1;
                best = best.max(and_val as i64 + x1 as i64 + x2 as i64);
                if sub == 0 {
                    break;
                }
                sub = (sub - 1) & comp;
            }
        }
        best
    }
}
