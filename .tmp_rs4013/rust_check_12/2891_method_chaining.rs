struct Solution;
// LeetCode 2891 - Method Chaining
// https://leetcode.com/problems/method-chaining/

impl Solution {
    pub fn find_heavy_animals(mut animals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        animals.retain(|r| r.len() > 3 && r[3] > 100);
        animals.sort_by(|a, b| b[3].cmp(&a[3]));
        animals.into_iter().map(|r| vec![r[0]]).collect()
    }
}

fn main() {}
