struct Solution;
// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

impl Solution {
    pub fn toggle_light_bulbs(bulbs: Vec<i32>) -> Vec<i32> {
        let mut st = [0; 101];
        for x in bulbs {
            st[x as usize] ^= 1;
        }
        (0..101).filter(|&i| st[i] == 1).map(|i| i as i32).collect()
    }
}
