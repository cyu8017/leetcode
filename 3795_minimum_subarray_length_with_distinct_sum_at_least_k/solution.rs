// LeetCode 3795 - Minimum Subarray Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/

use std::collections::HashMap;

impl Solution {
    pub fn min_length(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut ans = n as i32 + 1;
        let mut l = 0usize;
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut s = 0i64;
        for r in 0..n {
            let e = cnt.entry(nums[r]).or_insert(0);
            *e += 1;
            if *e == 1 {
                s += nums[r] as i64;
            }
            while s >= k as i64 {
                if (r - l + 1) as i32 < ans {
                    ans = (r - l + 1) as i32;
                }
                let e = cnt.get_mut(&nums[l]).unwrap();
                *e -= 1;
                if *e == 0 {
                    s -= nums[l] as i64;
                }
                l += 1;
            }
        }
        if ans > n as i32 { -1 } else { ans }
    }
}
