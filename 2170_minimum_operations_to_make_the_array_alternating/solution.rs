// LeetCode 2170 - Minimum Operations to Make the Array Alternating
// https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

use std::collections::HashMap;

impl Solution {
    fn top2(nums: &[i32], idxs: &[usize]) -> [i32; 4] {
        let mut freq = HashMap::new();
        for &i in idxs {
            *freq.entry(nums[i]).or_insert(0) += 1;
        }
        let mut a = 0;
        let mut ac = 0;
        let mut b = 0;
        let mut bc = 0;
        for (&v, &c) in &freq {
            if c > ac {
                b = a;
                bc = ac;
                a = v;
                ac = c;
            } else if c > bc {
                b = v;
                bc = c;
            }
        }
        [a, ac, b, bc]
    }

    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        if n == 1 {
            return 0;
        }
        let even: Vec<usize> = (0..nums.len()).step_by(2).collect();
        let odd: Vec<usize> = (1..nums.len()).step_by(2).collect();
        let e = Self::top2(&nums, &even);
        let o = Self::top2(&nums, &odd);
        if e[0] != o[0] {
            n - e[1] - o[1]
        } else {
            (n - e[1] - o[3]).min(n - e[3] - o[1])
        }
    }
}
