// LeetCode 2167 - Minimum Time to Remove All Cars Containing Illegal Goods
// https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

impl Solution {
    pub fn minimum_time(s: String) -> i32 {
        let n = s.len();
        let b = s.as_bytes();
        let mut left = vec![0; n];
        if b[0] == b'1' {
            left[0] = 1;
        }
        for i in 1..n {
            left[i] = left[i - 1];
            if b[i] == b'1' {
                left[i] = (i as i32 + 1).min(left[i - 1] + 2);
            }
        }
        let mut ans = left[n - 1];
        let mut right = 0;
        for i in (0..n).rev() {
            if b[i] == b'1' {
                right = (n as i32 - i as i32).min(right + 2);
            }
            let left_cost = if i > 0 { left[i - 1] } else { 0 };
            ans = ans.min(left_cost + right);
        }
        ans
    }
}
