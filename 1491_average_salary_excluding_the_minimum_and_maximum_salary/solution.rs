// LeetCode 1491 - Average Salary Excluding the Minimum and Maximum Salary
// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

impl Solution {
    pub fn average(salary: Vec<i32>) -> f64 {
        let sum: i32 = salary.iter().sum();
        let min = *salary.iter().min().unwrap();
        let max = *salary.iter().max().unwrap();
        (sum - min - max) as f64 / (salary.len() - 2) as f64
    }
}
