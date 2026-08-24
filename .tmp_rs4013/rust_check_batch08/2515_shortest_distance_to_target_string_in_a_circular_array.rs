struct Solution;
// LeetCode 2515 - Shortest Distance to Target String in a Circular Array
// https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

impl Solution {
    pub fn closest_target(words: Vec<String>, target: String, start_index: i32) -> i32 {
        let n = words.len() as i32;
        let mut best = -1;
        for i in 0..n {
            if words[i as usize] == target {
                let mut d = i - start_index;
                if d < 0 {
                    d = -d;
                }
                if n - d < d {
                    d = n - d;
                }
                if best < 0 || d < best {
                    best = d;
                }
            }
        }
        best
    }
}

fn main() {}
