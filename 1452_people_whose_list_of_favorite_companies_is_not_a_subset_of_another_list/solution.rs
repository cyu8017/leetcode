// LeetCode 1452 - People Whose List of Favorite Companies Is Not a Subset of Another List
// https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

use std::collections::HashSet;

impl Solution {
    pub fn people_indexes(favorite_companies: Vec<Vec<String>>) -> Vec<i32> {
        let sets: Vec<HashSet<&str>> = favorite_companies
            .iter()
            .map(|v| v.iter().map(|s| s.as_str()).collect())
            .collect();
        (0..sets.len())
            .filter(|&i| {
                !sets.iter().enumerate().any(|(j, t)| i != j && sets[i].is_subset(t))
            })
            .map(|i| i as i32)
            .collect()
    }
}
