// LeetCode 3200 - Maximum Height of a Triangle
// https://leetcode.com/problems/maximum-height-of-a-triangle/

impl Solution {
    pub fn max_height_of_triangle(red: i32, blue: i32) -> i32 {
        let mut ans = 0;
        for k in 0..2 {
            let mut c = [red, blue];
            let mut j = k;
            let mut i = 1;
            while i <= c[j] {
                c[j] -= i;
                ans = ans.max(i);
                i += 1;
                j ^= 1;
            }
        }
        ans
    }
}
