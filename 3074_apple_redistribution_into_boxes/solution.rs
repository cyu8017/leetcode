// LeetCode 3074 - Apple Redistribution into Boxes
// https://leetcode.com/problems/apple-redistribution-into-boxes/

impl Solution {
    pub fn minimum_boxes(apple: Vec<i32>, mut capacity: Vec<i32>) -> i32 {
        capacity.sort_unstable();
        let mut s: i32 = apple.iter().sum();
        let mut i = 1;
        loop {
            s -= capacity[capacity.len() - i];
            if s <= 0 {
                return i as i32;
            }
            i += 1;
        }
    }
}
