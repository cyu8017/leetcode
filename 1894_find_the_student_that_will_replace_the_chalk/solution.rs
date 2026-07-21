// LeetCode 1894 - Find the Student that Will Replace the Chalk
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

impl Solution {
    pub fn chalk_replacer(chalk: Vec<i32>, k: i32) -> i32 {
        let total: i64 = chalk.iter().map(|&c| c as i64).sum();
        let mut k = (k as i64) % total;
        for (index, &need) in chalk.iter().enumerate() {
            if k < need as i64 {
                return index as i32;
            }
            k -= need as i64;
        }
        0
    }
}
