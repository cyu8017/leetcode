struct Solution;
fn main() {}

// LeetCode 2815 - Max Pair Sum in an Array
// https://leetcode.com/problems/max-pair-sum-in-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn max_sum(nums: Vec<i32>) -> i32 {
        let mut best: HashMap<i32, i32> = HashMap::new();
        let mut ans = -1;
        for v in nums {
            let mut x = v;
            let mut md = 0;
            while x > 0 {
                md = md.max(x % 10);
                x /= 10;
            }
            if let Some(&prev) = best.get(&md) {
                ans = ans.max(prev + v);
                best.insert(md, prev.max(v));
            } else {
                best.insert(md, v);
            }
        }
        ans
    }
}
