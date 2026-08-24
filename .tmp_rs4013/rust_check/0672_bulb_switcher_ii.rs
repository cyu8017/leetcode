struct Solution;
// LeetCode 0672 - Bulb Switcher II
// https://leetcode.com/problems/bulb-switcher-ii/

impl Solution {
    pub fn flip_lights(n: i32, presses: i32) -> i32 {
        let n = n.min(3) as usize;
        if presses == 0 {
            return 1;
        }
        let one_press = [2, 3, 4];
        let two_press = [2, 4, 7];
        let many_press = [2, 4, 8];
        if presses == 1 {
            return one_press[n - 1];
        }
        if presses == 2 {
            return two_press[n - 1];
        }
        many_press[n - 1]
    }
}

fn main() {}
