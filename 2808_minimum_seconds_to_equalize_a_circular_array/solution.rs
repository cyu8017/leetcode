// LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_seconds(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut pos: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in nums.iter().enumerate() {
            pos.entry(v).or_default().push(i);
        }
        let mut ans = n as i32;
        for p in pos.values() {
            let mut max_gap = 0;
            for i in 0..p.len() {
                let gap = if i + 1 < p.len() {
                    p[i + 1] - p[i]
                } else {
                    p[0] + n - p[i]
                };
                max_gap = max_gap.max(gap / 2);
            }
            ans = ans.min(max_gap as i32);
        }
        ans
    }
}
