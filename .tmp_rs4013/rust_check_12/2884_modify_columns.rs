struct Solution;
// LeetCode 2884 - Modify Columns
// https://leetcode.com/problems/modify-columns/

impl Solution {
    pub fn modify_salary_column(employees: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        employees
            .into_iter()
            .map(|mut r| {
                if let Some(last) = r.last_mut() {
                    *last *= 2;
                }
                r
            })
            .collect()
    }
}

fn main() {}
