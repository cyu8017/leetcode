// LeetCode 3717 - Minimum Operations to Make the Array Beautiful
// https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

use std::collections::HashMap;

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut f: HashMap<i32, i32> = HashMap::new();
        f.insert(nums[0], 0);
        for i in 1..nums.len() {
            let x = nums[i];
            let mut g: HashMap<i32, i32> = HashMap::new();
            for (&pre, &s) in &f {
                let mut cur = (x + pre - 1) / pre * pre;
                while cur <= 100 {
                    let val = s + (cur - x);
                    g.entry(cur)
                        .and_modify(|old| {
                            if *old > val {
                                *old = val;
                            }
                        })
                        .or_insert(val);
                    cur += pre;
                }
            }
            f = g;
        }
        f.values().copied().min().unwrap_or(0)
    }
}
