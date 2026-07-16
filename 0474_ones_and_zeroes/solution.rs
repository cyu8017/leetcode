// LeetCode 0474 - Ones and Zeroes
// https://leetcode.com/problems/ones-and-zeroes/

impl Solution {
    pub fn find_max_form(strs: Vec<String>, m: i32, n: i32) -> i32 {
        let m = m as usize;
        let n = n as usize;
        let mut dp = vec![vec![0; n + 1]; m + 1];
        for string in strs {
            let zeros = string.chars().filter(|ch| *ch == '0').count();
            let ones = string.len() - zeros;
            for zero in (zeros..=m).rev() {
                for one in (ones..=n).rev() {
                    dp[zero][one] = dp[zero][one]
                        .max(dp[zero - zeros][one - ones] + 1);
                }
            }
        }
        dp[m][n] as i32
    }
}
