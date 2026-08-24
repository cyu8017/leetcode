// LeetCode 2078 - Two Furthest Houses With Different Colors
// https://leetcode.com/problems/two-furthest-houses-with-different-colors/

impl Solution {
    pub fn max_distance(colors: Vec<i32>) -> i32 {
        let n = colors.len();
        let mut ans = 0;
        for i in 0..n {
            if colors[i] != colors[0] {
                ans = ans.max(i as i32);
            }
            if colors[i] != colors[n - 1] {
                ans = ans.max((n - 1 - i) as i32);
            }
        }
        ans
    }
}
