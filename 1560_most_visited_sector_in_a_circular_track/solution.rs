// LeetCode 1560 - Most Visited Sector in a Circular Track
// https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

impl Solution {
    pub fn most_visited(n: i32, rounds: Vec<i32>) -> Vec<i32> {
        let start = rounds[0];
        let end = *rounds.last().unwrap();
        if start <= end {
            (start..=end).collect()
        } else {
            (1..=end).chain(start..=n).collect()
        }
    }
}
