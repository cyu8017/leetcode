struct Solution;
// LeetCode 2881 - Create a New Column
// https://leetcode.com/problems/create-a-new-column/

impl Solution {
    pub fn create_bonus_column(employees: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        employees
            .into_iter()
            .map(|mut r| {
                let salary = *r.last().unwrap_or(&0);
                r.push(salary * 2);
                r
            })
            .collect()
    }
}

fn main() {}
