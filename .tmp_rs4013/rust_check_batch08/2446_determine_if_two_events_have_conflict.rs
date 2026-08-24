struct Solution;
// LeetCode 2446 - Determine if Two Events Have Conflict
// https://leetcode.com/problems/determine-if-two-events-have-conflict/

impl Solution {
    pub fn have_conflict(event1: Vec<String>, event2: Vec<String>) -> bool {
        event1[0] <= event2[1] && event2[0] <= event1[1]
    }
}

fn main() {}
