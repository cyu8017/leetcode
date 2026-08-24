struct Solution;
// LeetCode 3434 - Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

use std::collections::HashSet;

impl Solution {
    pub fn max_frequency(nums: Vec<i32>, k: i32) -> i32 {
        let base = nums.iter().filter(|&&x| x == k).count() as i32;
        let mut ans = base;
        let uniq: HashSet<i32> = nums.iter().copied().collect();
        for v in uniq {
            if v == k {
                continue;
            }
            let mut best = 0;
            let mut cur = 0;
            for &x in &nums {
                let delta = if x == v {
                    1
                } else if x == k {
                    -1
                } else {
                    0
                };
                cur += delta;
                if cur < 0 {
                    cur = 0;
                }
                if cur > best {
                    best = cur;
                }
            }
            if base + best > ans {
                ans = base + best;
            }
        }
        ans
    }
}

fn main() {}
