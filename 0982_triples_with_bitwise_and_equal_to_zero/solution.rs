// LeetCode 0982 - Triples with Bitwise AND Equal To Zero
// https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

use std::collections::HashMap;

impl Solution {
    pub fn count_triplets(nums: Vec<i32>) -> i32 {
        let mut cnt = HashMap::new();
        for &a in &nums {
            for &b in &nums {
                *cnt.entry(a & b).or_insert(0) += 1;
            }
        }
        let mut ans = 0;
        for &c in &nums {
            for (&ab, &times) in &cnt {
                if (ab & c) == 0 {
                    ans += times;
                }
            }
        }
        ans
    }
}
