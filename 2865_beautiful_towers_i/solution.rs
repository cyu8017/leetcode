// LeetCode 2865 - Beautiful Towers I
// https://leetcode.com/problems/beautiful-towers-i/

impl Solution {
    pub fn maximum_sum_of_heights(heights: Vec<i32>) -> i64 {
        let n = heights.len();
        let mut ans = 0i64;
        for peak in 0..n {
            let mut sum = heights[peak] as i64;
            let mut mn = heights[peak];
            for i in (0..peak).rev() {
                if heights[i] < mn {
                    mn = heights[i];
                }
                sum += mn as i64;
            }
            mn = heights[peak];
            for i in peak + 1..n {
                if heights[i] < mn {
                    mn = heights[i];
                }
                sum += mn as i64;
            }
            ans = ans.max(sum);
        }
        ans
    }
}
