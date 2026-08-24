// LeetCode 3846 - Total Distance to Type a String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

use std::collections::HashMap;

impl Solution {
    pub fn total_distance(s: String) -> i32 {
        let keys = ["qwertyuiop", "asdfghjkl", "zxcvbnm"];
        let mut pos = HashMap::new();
        for (i, row) in keys.iter().enumerate() {
            for (j, c) in row.chars().enumerate() {
                pos.insert(c, (i as i32, j as i32));
            }
        }
        let mut pre = 'a';
        let mut ans = 0;
        for cur in s.chars() {
            let p1 = pos[&pre];
            let p2 = pos[&cur];
            ans += (p1.0 - p2.0).abs() + (p1.1 - p2.1).abs();
            pre = cur;
        }
        ans
    }
}
