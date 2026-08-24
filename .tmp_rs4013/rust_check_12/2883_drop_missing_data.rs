struct Solution;
// LeetCode 2883 - Drop Missing Data
// https://leetcode.com/problems/drop-missing-data/

impl Solution {
    pub fn drop_missing_data(students: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        students
            .into_iter()
            .filter(|r| r.len() < 2 || r[1] != 0)
            .collect()
    }
}

fn main() {}
