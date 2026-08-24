// LeetCode 3096 - Minimum Levels to Gain More Points
// https://leetcode.com/problems/minimum-levels-to-gain-more-points/

impl Solution {
    pub fn minimum_levels(possible: Vec<i32>) -> i32 {
        let s: i32 = possible.iter().map(|&x| if x == 0 { -1 } else { x }).sum();
        let mut t = 0;
        for i in 0..possible.len() - 1 {
            let x = if possible[i] == 0 { -1 } else { possible[i] };
            t += x;
            if t > s - t {
                return i as i32 + 1;
            }
        }
        -1
    }
}
