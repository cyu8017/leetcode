// LeetCode 1700 - Number of Students Unable to Eat Lunch
// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

impl Solution {
    pub fn count_students(students: Vec<i32>, sandwiches: Vec<i32>) -> i32 {
        let mut c = [0i32; 2];
        for &s in &students {
            c[s as usize] += 1;
        }
        for (i, &x) in sandwiches.iter().enumerate() {
            if c[x as usize] == 0 {
                return (students.len() - i) as i32;
            }
            c[x as usize] -= 1;
        }
        0
    }
}
