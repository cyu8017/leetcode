// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/

impl Solution {
    pub fn count_seniors(details: Vec<String>) -> i32 {
        let mut ans = 0;
        for d in &details {
            let b = d.as_bytes();
            let age = (b[11] - b'0') as i32 * 10 + (b[12] - b'0') as i32;
            if age > 60 {
                ans += 1;
            }
        }
        ans
    }
}
