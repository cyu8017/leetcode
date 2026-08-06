// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

use std::collections::HashMap;

impl Solution {
    pub fn max_equal_freq(nums: Vec<i32>) -> i32 {
        let mut count = HashMap::new();
        let mut frequencies = HashMap::new();
        let mut answer = 0;
        for (i, &x) in nums.iter().enumerate() {
            let old = *count.get(&x).unwrap_or(&0);
            if old > 0 {
                let e = frequencies.get_mut(&old).unwrap();
                *e -= 1;
                if *e == 0 {
                    frequencies.remove(&old);
                }
            }
            count.insert(x, old + 1);
            *frequencies.entry(old + 1).or_insert(0) += 1;
            let high = *frequencies.keys().max().unwrap();
            let idx = i as i32 + 1;
            if high == 1
                || frequencies.get(&high).copied().unwrap_or(0) * high + 1 == idx
                || (frequencies.get(&high).copied().unwrap_or(0) == 1
                    && frequencies.get(&(high - 1)).copied().unwrap_or(0) * (high - 1) + high
                        == idx)
            {
                answer = idx;
            }
        }
        answer
    }
}
