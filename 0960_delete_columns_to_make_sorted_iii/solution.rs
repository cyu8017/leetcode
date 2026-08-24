// LeetCode 0960 - Delete Columns to Make Sorted III
// https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let m = strs[0].len();
        let mut dp = vec![1; m];
        for j in 0..m {
            for i in 0..j {
                let ok = strs.iter().all(|row| row.as_bytes()[i] <= row.as_bytes()[j]);
                if ok {
                    dp[j] = dp[j].max(dp[i] + 1);
                }
            }
        }
        m as i32 - *dp.iter().max().unwrap()
    }
}
