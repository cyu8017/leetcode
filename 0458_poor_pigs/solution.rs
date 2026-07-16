// LeetCode 0458 - Poor Pigs
// https://leetcode.com/problems/poor-pigs/

impl Solution {
    pub fn poor_pigs(buckets: i32, minutes_to_die: i32, minutes_to_test: i32) -> i32 {
        let states = minutes_to_test / minutes_to_die + 1;
        let mut pigs = 0;
        let mut capacity = 1;
        while capacity < buckets {
            pigs += 1;
            capacity *= states;
        }
        pigs
    }
}
