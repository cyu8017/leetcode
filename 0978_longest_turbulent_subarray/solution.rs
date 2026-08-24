// LeetCode 0978 - Longest Turbulent Subarray
// https://leetcode.com/problems/longest-turbulent-subarray/

impl Solution {
    pub fn max_turbulence_size(arr: Vec<i32>) -> i32 {
        let mut ans = 1;
        let mut cur = 1;
        for i in 1..arr.len() {
            if arr[i] == arr[i - 1] {
                cur = 1;
            } else if i == 1
                || (arr[i] - arr[i - 1]) as i64 * (arr[i - 1] - arr[i - 2]) as i64 < 0
            {
                cur += 1;
            } else {
                cur = 2;
            }
            ans = ans.max(cur);
        }
        ans
    }
}
