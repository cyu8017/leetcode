// LeetCode 1436 - Destination City
// https://leetcode.com/problems/destination-city/

use std::collections::HashSet;

impl Solution {
    pub fn dest_city(paths: Vec<Vec<String>>) -> String {
        let starts: HashSet<&str> = paths.iter().map(|p| p[0].as_str()).collect();
        paths
            .into_iter()
            .find(|p| !starts.contains(p[1].as_str()))
            .unwrap()[1]
            .clone()
    }
}
