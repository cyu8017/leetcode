// LeetCode 2879 - Display the First Three Rows
// https://leetcode.com/problems/display-the-first-three-rows/

impl Solution {
    pub fn select_first_rows(employees: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        employees.into_iter().take(3).collect()
    }
}
