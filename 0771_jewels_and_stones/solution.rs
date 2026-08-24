// LeetCode 0771 - Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

use std::collections::HashSet;

impl Solution {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        let jewel_set: HashSet<char> = jewels.chars().collect();
        stones.chars().filter(|ch| jewel_set.contains(ch)).count() as i32
    }
}
