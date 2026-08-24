// LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
// https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

use std::collections::HashMap;

impl Solution {
    pub fn min_mirror_pair_distance(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut pos = HashMap::new();
        let mut ans = n + 1;
        let reverse = |mut x: i32| {
            let mut y = 0;
            while x > 0 {
                y = y * 10 + x % 10;
                x /= 10;
            }
            y
        };
        for (i, &x) in nums.iter().enumerate() {
            if let Some(&p) = pos.get(&x) {
                ans = ans.min(i as i32 - p);
            }
            pos.insert(reverse(x), i as i32);
        }
        if ans > n { -1 } else { ans }
    }
}
