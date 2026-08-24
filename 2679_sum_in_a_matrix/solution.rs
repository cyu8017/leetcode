// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

impl Solution {
    pub fn matrix_sum(mut nums: Vec<Vec<i32>>) -> i32 {
        for row in &mut nums {
            row.sort_unstable();
        }
        let mut ans = 0;
        let n = nums[0].len();
        for j in 0..n {
            let mut mx = 0;
            for row in &nums {
                mx = mx.max(row[j]);
            }
            ans += mx;
        }
        ans
    }
}
