// LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

use std::collections::HashMap;

impl Solution {
    pub fn find_matrix(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut freq = HashMap::new();
        let mut ans: Vec<Vec<i32>> = Vec::new();
        for x in nums {
            let f = *freq.get(&x).unwrap_or(&0);
            if f == ans.len() {
                ans.push(Vec::new());
            }
            ans[f].push(x);
            *freq.entry(x).or_insert(0) += 1;
        }
        ans
    }
}
