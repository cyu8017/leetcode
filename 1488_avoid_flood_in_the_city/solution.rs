// LeetCode 1488 - Avoid Flood in The City
// https://leetcode.com/problems/avoid-flood-in-the-city/

use std::collections::HashMap;

impl Solution {
    pub fn avoid_flood(rains: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![-1; rains.len()];
        let mut full = HashMap::new();
        let mut dry = Vec::new();
        for (i, &lake) in rains.iter().enumerate() {
            if lake == 0 {
                dry.push(i);
                ans[i] = 1;
            } else {
                if let Some(&prev) = full.get(&lake) {
                    let j = dry.partition_point(|&d| d <= prev);
                    if j == dry.len() {
                        return vec![];
                    }
                    let day = dry.remove(j);
                    ans[day] = lake;
                }
                full.insert(lake, i);
            }
        }
        ans
    }
}
