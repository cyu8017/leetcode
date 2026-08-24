struct Solution;
// LeetCode 2880 - Select Data
// https://leetcode.com/problems/select-data/

impl Solution {
    pub fn select_data(students: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        students
            .into_iter()
            .filter(|r| !r.is_empty() && r[0] == 101)
            .map(|r| r[1..].to_vec())
            .collect()
    }
}

fn main() {}
