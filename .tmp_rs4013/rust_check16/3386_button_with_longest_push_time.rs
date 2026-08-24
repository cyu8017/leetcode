struct Solution;
// LeetCode 3386 - Button with Longest Push Time
// https://leetcode.com/problems/button-with-longest-push-time/

impl Solution {
    pub fn button_with_longest_time(events: Vec<Vec<i32>>) -> i32 {
        let mut best_t = events[0][1];
        let mut best_i = events[0][0];
        for i in 1..events.len() {
            let t = events[i][1] - events[i - 1][1];
            if t > best_t || (t == best_t && events[i][0] < best_i) {
                best_t = t;
                best_i = events[i][0];
            }
        }
        best_i
    }
}

fn main() {}
