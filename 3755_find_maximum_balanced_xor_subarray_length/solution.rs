// LeetCode 3755 - Find Maximum Balanced Xor Subarray Length
// https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/

use std::collections::HashMap;

impl Solution {
    pub fn max_balanced_subarray(nums: Vec<i32>) -> i32 {
        let mut d: HashMap<i64, i32> = HashMap::new();
        let mut a = 0i32;
        let mut b = nums.len() as i32;
        let mut ans = 0;
        d.insert(b as i64, -1);
        for (i, &x) in nums.iter().enumerate() {
            a ^= x;
            if x % 2 == 0 {
                b += 1;
            } else {
                b -= 1;
            }
            let key = ((a as i64) << 32) | (b as i64);
            if let Some(&prev) = d.get(&key) {
                ans = ans.max(i as i32 - prev);
            } else {
                d.insert(key, i as i32);
            }
        }
        ans
    }
}
