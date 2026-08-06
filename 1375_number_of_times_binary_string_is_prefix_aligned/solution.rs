// LeetCode 1375 - Number of Times Binary String Is Prefix-Aligned
// https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

impl Solution {
    pub fn num_times_all_blue(flips: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut mx = 0;
        for (i, &x) in flips.iter().enumerate() {
            mx = mx.max(x);
            if mx == (i as i32 + 1) {
                ans += 1;
            }
        }
        ans
    }
}
